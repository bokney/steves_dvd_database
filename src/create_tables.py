
# from data_types import Format, Person, Item
import sqlite3
from get_db_connection import get_db_connection

def create_format_table():
    con, cur = get_db_connection()
    if con and cur:
        try:
            cur.execute(
                """CREATE TABLE IF NOT EXISTS format(
                    id INTEGER PRIMARY KEY,
                    name TEXT
                );""")
        finally:
            cur.close()
            con.close()

def create_person_table():
    con, cur = get_db_connection()
    if con and cur:
        try:
            cur.execute(
                """CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT
                );""")
        finally:
            cur.close()
            con.close()

def create_item_table():
    con, cur = get_db_connection()
    if con and cur:
        try:
            cur.execute(
                """CREATE TABLE IF NOT EXISTS item(
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    barcode TEXT
                );""")
        finally:
            cur.close()
            con.close()

def create_tables():
    create_format_table()
    create_person_table()
    create_item_table()
