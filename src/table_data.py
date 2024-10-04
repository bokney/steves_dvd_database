
from data_types import Format, Person, Item
import sqlite3

formats: list[Format] = []
actors: list[Actor] = []
directors: list[Director] = []
items: list[Item] = []

database_name = "steves_dvd_database_test"

# # # # FORMAT # # # #

def create_format_table():
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS format(
            id INTEGER PRIMARY KEY,
            name TEXT
        );""")
    con.close()

def insert_format(format: Format):
    con = sqlite3.connect(database_name)
    # cur = con.cursor()
    con.execute("INSERT INTO format(name) VALUES (?);", (format.name,))
    con.commit()
    con.close()

def retrieve_format_table():
    formats.clear()
    con = sqlite3.connect(database_name)
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
    
# # # # ACTOR # # # #

def create_actor_table():
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS actor(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        );"""
        )
    con.close()

def insert_actor(actor: Actor):
    con = sqlite3.connect(database_name)
    # cur = con.cursor()
    con.execute("INSERT INTO actor(first_name, last_name) VALUES (?, ?);",
                (format.first_name,), (format.last_name,))
    con.commit()
    con.close()

def retrieve_actor_table():
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    cur.execute(
        """SELECT * FROM actor;"""
    )
    output = cur.fetchall()
    con.close()
    return output

# # # # DIRECTOR # # # #

def create_director_table():
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS director(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        );"""
        )
    con.close()

def retrieve_director_table():
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    cur.execute(
        """SELECT * FROM director;"""
    )
    output = cur.fetchall()
    con.close()
    return output

# # # # ITEM # # # #

def create_item_table():
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS item(
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            barcode TEXT
        );"""
        )
    con.close()

def retrieve_item_table():
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    cur.execute(
        """SELECT * FROM item;"""
    )
    output = cur.fetchall()
    con.close()
    return output

# # # # ---- # # # #

def create_all_tables():
    create_format_table()
    create_actor_table()
    create_director_table()
    create_item_table()

def retrieve_all_tables():
    return (
        retrieve_format_table(),
        retrieve_actor_table(),
        retrieve_director_table(),
        retrieve_item_table()
    )

a_format = Format(
    name = "DVD"
)

an_actor = Actor(
    first_name = "",
    last_name = ""
)
insert_actor(an_actor)

a_director = Director(
    first_name = "Jordan",
    last_name = "Peele"
)

create_all_tables()
# insert_format(a_format)
# for table in retrieve_all_tables():
#     print(table)
retrieve_format_table()
for f in formats:
    print(f)
