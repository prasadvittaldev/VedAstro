"""Storage for API error log entries."""

import sqlite3
from dataclasses import dataclass, field
from datetime import datetime

from ..sqlite_db import connection


def _ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS openapi_error_book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            endpoint TEXT,
            error TEXT,
            ts DATETIME
        )
        """
    )


@dataclass
class OpenAPIErrorBook:
    endpoint: str
    error: str
    ts: datetime = field(default_factory=datetime.utcnow)

    def save(self) -> None:
        with connection() as conn:
            _ensure_table(conn)
            conn.execute(
                "INSERT INTO openapi_error_book (endpoint, error, ts) VALUES (?, ?, ?)",
                (self.endpoint, self.error, self.ts),
            )
