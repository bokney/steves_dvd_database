# import pandas as pd
# format = pd.DataFrame()

import sqlite3

con = sqlite3.connect("steves_dvd_database_test")

cur = con.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS item(
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        barcode TEXT        
    );"""
    )

con.execute(
    """INSERT INTO item(title, description, barcode) VALUES ("A", "B", "C");"""
)
con.execute(
    """INSERT INTO item(title, description, barcode) VALUES ("1", "2", "3");"""
)
con.execute(
    """INSERT INTO item(title, description, barcode) VALUES ("🧸", "🧸", "🧸");"""
)

con.commit()

cur.execute(
    """SELECT * FROM item;"""
)

output = cur.fetchall()

con.close()

for row in output:
    print(row)

# from pydantic import BaseModel, Field
# from uuid import UUID, uuid4

# class Format(BaseModel):
#     # id: UUID = Field(default_factory=uuid4)
#     name: str

# class Actor(BaseModel):
#     # id: int
#     first_name: str
#     last_name: str

# class Director(BaseModel):
#     # id: int
#     first_name: str
#     last_name: str

# class Item(BaseModel):
#     # id: int
#     title: str
#     description: str | None
#     barcode: str | None
#     format: Format | None
#     director: list[Director] | None
#     actors: list[Actor] | None

# def load_items(filepath: str) -> list[Item]:
#     # load formats
#     # load actors
#     # load directors
#     # load items
#     pass

# blu_ray = Format(name='Blu-Ray')
# franklin = Director(
#     first_name='Franklin',
#     last_name='Schaffner'
# )

# an_item = Item(
#     title='Planet of the Apes',
#     description=None,
#     barcode='012345ABCD',
#     format=blu_ray,
#     director=[franklin],
#     actors=None
#     )

# print(an_item)
# print(an_item.model_dump_json())

# # def add_item(item):

# #     pass

