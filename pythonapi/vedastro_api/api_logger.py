"""Simple request/response logging backed by SQLite."""

import sqlite3
from typing import Dict, List

from .sqlite_db import connection


def _ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS api_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            endpoint TEXT,
            status_code INTEGER,
            ts DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


def log_request(endpoint: str, status_code: int) -> None:
    """Record an API call and its response status code."""
    with connection() as conn:
        _ensure_table(conn)
        conn.execute(
            "INSERT INTO api_log (endpoint, status_code) VALUES (?, ?)",
            (endpoint, status_code),
        )


def fetch_logs() -> List[Dict[str, int]]:
    """Return all recorded log entries."""
    with connection() as conn:
        _ensure_table(conn)
        rows = conn.execute(
            "SELECT endpoint, status_code FROM api_log ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]
