
import sqlite3
import os

def get_db_connection() -> tuple[
      sqlite3.Connection | None, sqlite3.Cursor | None]:
    db_name = os.getenv('DATABASE_NAME')
    try:
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        print("Succesfully connected!")
        return con, cur
    except sqlite3.Error as e:
        print(f"Error! Failed to connect to {db_name}: {e}")
        return None, None
