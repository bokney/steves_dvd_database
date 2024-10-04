
from data_types import Format, Person, Item
# from dotenv import load_dotenv
import sqlite3
import os

def insert_format(self, data: Format):
    con = sqlite3.connect(os.getenv('DATABASE_NAME'))
    con.execute("INSERT INTO format(name) VALUES (?);", (data.name,))
    con.commit()
    con.close()

def insert_person(person: Person):
    con = sqlite3.connect(os.getenv('DATABASE_NAME'))
    con.execute("""
                INSERT INTO person(
                    first_name,
                    last_name
                ) VALUES (?, ?);
                """,
                (person.first_name,),
                (person.last_name,))
    con.commit()
    con.close()

def insert_item(item: Item):
    con = sqlite3.connect(os.getenv('DATABASE_NAME'))
    con.execute("""
                INSERT INTO item(
                    title,
                    description,
                    barcode,
                    format,
                    directors,
                    actors
                ) VALUES (?, ?);
                """,
                (item.title,),
                (item.description,)
                (item.barcode,)
                (item.format,)
                (item.directors,)
                (item.actors,))
    con.commit()
    con.close()
