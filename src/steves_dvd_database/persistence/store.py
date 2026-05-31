
import sqlite3
from pathlib import Path

from .models import Media, Copy


def save_media(db_path: Path, title: str, release_year: int | None = None, rating: int | None = None) -> int | None:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "INSERT INTO media (title, release_year, rating) VALUES (?, ?, ?)",
            (title, release_year, rating)
        )
        return cursor.lastrowid


def load_media(db_path: Path, id: int | None = None, title: str | None = None) -> list[Media]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        query = "SELECT id, title, release_year, rating FROM media WHERE 1=1"
        params = []
        
        if id:
            query += " AND id = ?"
            params.append(id)
        if title:
            query += " AND title LIKE ?"
            params.append(f"%{title}%")
            
        records = conn.execute(query, params).fetchall()
        return [Media(**dict(record)) for record in records]


def save_copy(db_path: Path, media_id: int, format: str, notes: str | None = None) -> int | None:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "INSERT INTO copies (media_id, format, notes) VALUES (?, ?, ?)",
            (media_id, format, notes)
        )
        return cursor.lastrowid


def load_copies(db_path: Path, id: int | None = None, title: str | None = None) -> list[Copy]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        
        query = """
            SELECT c.id, c.media_id, c.format, c.notes 
            FROM copies c
            LEFT JOIN media m ON c.media_id = m.id
            WHERE 1=1
        """
        params = []
        
        if id:
            query += " AND c.id = ?"
            params.append(id)
        if title:
            query += " AND m.title LIKE ?"
            params.append(f"%{title}%")
            
        records = conn.execute(query, params).fetchall()
        return [Copy(**dict(record)) for record in records]
