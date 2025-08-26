import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

DB_PATH = os.getenv("VEDASTRO_DB", str(Path(__file__).with_name("vedastro.db")))
_CONN: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
    """Return a cached SQLite connection using the configured path."""
    global _CONN
    if _CONN is None:
        _CONN = sqlite3.connect(DB_PATH, check_same_thread=False)
        _CONN.row_factory = sqlite3.Row
    return _CONN


@contextmanager
def connection() -> Iterator[sqlite3.Connection]:
    """Context manager that yields a database connection and commits on exit."""
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    finally:
        pass
