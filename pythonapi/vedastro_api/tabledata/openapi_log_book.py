"""Storage for general API log entries."""

import sqlite3
from dataclasses import dataclass, field
from datetime import datetime

from ..sqlite_db import connection


def _ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS openapi_log_book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            endpoint TEXT,
            message TEXT,
            ts DATETIME
        )
        """
    )


@dataclass
class OpenAPILogBook:
    endpoint: str
    message: str
    ts: datetime = field(default_factory=datetime.utcnow)

    def save(self) -> None:
        with connection() as conn:
            _ensure_table(conn)
            conn.execute(
                "INSERT INTO openapi_log_book (endpoint, message, ts) VALUES (?, ?, ?)",
                (self.endpoint, self.message, self.ts),
            )
