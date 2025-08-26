"""Storage for API call status entries."""

import sqlite3
from dataclasses import dataclass, field
from datetime import datetime

from ..sqlite_db import connection


def _ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS call_status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            endpoint TEXT,
            status TEXT,
            ts DATETIME
        )
        """
    )


@dataclass
class CallStatus:
    endpoint: str
    status: str
    ts: datetime = field(default_factory=datetime.utcnow)

    def save(self) -> None:
        with connection() as conn:
            _ensure_table(conn)
            conn.execute(
                "INSERT INTO call_status (endpoint, status, ts) VALUES (?, ?, ?)",
                (self.endpoint, self.status, self.ts),
            )
