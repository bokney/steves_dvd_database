
from data_types import Format, Person, Item
from create_tables import create_tables
from insert import insert_format
from read import read_format

formats: list[Format] = []
people: list[Person] = []
items: list[Item] = []

def init():
    print("Welcome")
    create_tables()
    return select

def select():
    print("Select option:")
    print("\
          [c] - Create\n\
          [r] - Read\n\
          [u] - Update\n\
          [d] - Delete\n\
          [e] - Exit\
          ")
    response = input().lower()
    match response:
        case "c":
            return create
        case "r":
            return read
        case "u":
            return update
        case "d":
            return delete
        case "e":
            return exit
        case _:
            print("Incorrect input")
            return select

def create():
    print("What to create?")
    print("\
          [f] - Format\n\
          [p] - Person\n\
          [i] - Item\n\
          [b] - Back\
          ")
    response = input().lower()
    match response:
        case "f":
            create_format()
        case "p":
            return format
        case "i":
            return format
        case "b":
            return format
        case _:
            print("Incorrect input")
            return select
    return select

def create_format():
    print("Enter format type name:")
    response = input()
    new_format = Format(response)
    insert_format(new_format)
    print(f"Inserted {new_format}")



def read():
    print("What to read?")
    print("\
          [f] - Format\n\
          [a] - Actor\n\
          [d] - Director\n\
          [i] - Item\n\
          [b] - Back\
          ")
    response = input().lower()
    match response:
        case "f":
            read_format()
        case "p":
            return select
        case "i":
            return select
        case "b":
            return select
        case _:
            print("Incorrect input")
            return select
    return select

def update():
    print("Update:")
    return select

def delete():
    print("Delete:")
    return select

def run(state):
    return state()
