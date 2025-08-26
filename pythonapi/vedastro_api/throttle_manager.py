"""Simple IP-based throttling using SQLite to track request times."""

import sqlite3
import time

from .sqlite_db import connection


def _ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS throttle (
            ip TEXT,
            ts REAL
        )
        """
    )


def is_allowed(client_ip: str, limit: int, window_seconds: int) -> bool:
    """Return True if the client is within the allowed request rate."""
    now = time.time()
    window_start = now - window_seconds
    with connection() as conn:
        _ensure_table(conn)
        conn.execute("DELETE FROM throttle WHERE ts < ?", (window_start,))
        count = conn.execute(
            "SELECT COUNT(*) FROM throttle WHERE ip = ?", (client_ip,)
        ).fetchone()[0]
        if count >= limit:
            return False
        conn.execute("INSERT INTO throttle (ip, ts) VALUES (?, ?)", (client_ip, now))
    return True
