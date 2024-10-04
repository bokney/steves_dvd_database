
from data_types import Format, Actor, Director, Item
from table_data import formats, actors, directors, items

def assign_name():
    print("Enter item name:")
    return input("↳")

def assign_description():
    print("Enter item description:")
    return input("↳")

def assign_barcode():
    print("Enter item barcode:")
    return input("↳")

def select_format():
    print("Pick an existing format or add a new one")

def select_directors():
    print("Pick an existing director or add a new one")

def select_actors():
    print("Pick an existing actor or add a new one")

def add_item():

    name = assign_name()
    if not name:
        pass
    description = assign_description()
    barcode = assign_barcode()
    format = select_format()
    directors = select_directors()
    actors = select_actors()

    items.append(Item(
        name = name,
        description = description,
        barcode = barcode,
        format = format,
        directors = directors,
        actors = actors
    ))

    
