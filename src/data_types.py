
from pydantic import BaseModel

class Format(BaseModel):
    name: str

class Person(BaseModel):
    first_name: str
    last_name: str

class Item(BaseModel):
    title: str
    description: str | None
    barcode: str | None
    format: Format | None
    directors: list[Person] | None
    actors: list[Person] | None
