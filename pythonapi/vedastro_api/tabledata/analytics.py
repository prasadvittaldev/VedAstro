"""Simple analytics counter storage."""

import sqlite3
from dataclasses import dataclass

from ..sqlite_db import connection


def _ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS analytics (
            endpoint TEXT PRIMARY KEY,
            count INTEGER
        )
        """
    )


@dataclass
class Analytics:
    endpoint: str
    count: int = 0

    def increment(self, amount: int = 1) -> None:
        with connection() as conn:
            _ensure_table(conn)
            conn.execute(
                (
                    "INSERT INTO analytics(endpoint, count) VALUES(?, ?) "
                    "ON CONFLICT(endpoint) DO UPDATE SET count = count + excluded.count"
                ),
                (self.endpoint, amount),
            )
