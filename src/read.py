
from data_types import Format, Person, Item
from app import formats, people, items
# from dotenv import load_dotenv
import os
import sqlite3

def read_format():
    formats.clear()
    con = sqlite3.connect(os.getenv('DATABASE_NAME'))
    cur = con.cursor()
    cur.execute(
        """SELECT name FROM format;"""
    )
    output = cur.fetchall()
    cur.close()
    con.close()
    for f in output:
        formats.append(Format(
            name = f[0]
        ))

def read_person():
    people.clear()
    con = sqlite3.connect(os.getenv('DATABASE_NAME'))
    cur = con.cursor()
    cur.execute(
        """SELECT first_name, last_name FROM people;"""
    )
    output = cur.fetchall()
    cur.close()
    con.close()
    for f in output:
        formats.append(Person(
            first_name = f[0],
            last_name = f[1]
        ))
