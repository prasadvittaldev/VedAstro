"""Caching geolocation lookups."""

import sqlite3
from dataclasses import dataclass, field
from datetime import datetime

from ..sqlite_db import connection


def _ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS geolocation_cache (
            name TEXT PRIMARY KEY,
            latitude REAL,
            longitude REAL,
            ts DATETIME
        )
        """
    )


@dataclass
class GeoLocationCache:
    name: str
    latitude: float
    longitude: float
    ts: datetime = field(default_factory=datetime.utcnow)

    def save(self) -> None:
        with connection() as conn:
            _ensure_table(conn)
            conn.execute(
                (
                    "INSERT OR REPLACE INTO geolocation_cache"
                    "(name, latitude, longitude, ts) VALUES(?, ?, ?, ?)"
                ),
                (self.name, self.latitude, self.longitude, self.ts),
            )
