
import sqlite3
from pathlib import Path


MEDIA_SCHEMA = """
    CREATE TABLE IF NOT EXISTS media (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255) NOT NULL,
        release_year INTEGER,
        rating INTEGER CHECK (rating >= 1 AND rating <= 5)
    );
"""

COPY_SCHEMA = """
    CREATE TABLE IF NOT EXISTS copies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        media_id INTEGER REFERENCES media(id),
        format TEXT NOT NULL,
        notes TEXT
    );
"""


def init_db(db_path: Path):
    with sqlite3.connect(db_path) as conn:
        conn.execute(MEDIA_SCHEMA)
        conn.execute(COPY_SCHEMA)
