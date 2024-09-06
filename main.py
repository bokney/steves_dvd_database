from db.connection import connect_to_db, close_db_connection
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pg8000.native import identifier
from util import sort_it_into_dict, sort_them_into_list

app = FastAPI()

@app.get("/")
def read_root() -> str:
    return "server is running ✅"

class Item(BaseModel):
    name: str
    description: str
    
@app.post("/items")
def create_item(item: Item):
    query_str = f"""
    INSERT INTO items (name, description)
    VALUES (:name, :description)
    RETURNING *;
    """
    db = connect_to_db()
    result = db.run(query_str, name=item.name, description=item.description)
    close_db_connection(db)
    sorted_dict = sort_it_into_dict(result[0], db.columns)
    return sorted_dict

orderables = ['ASC', 'DESC']
sortables = ["item_id", "name", "description"]

@app.get("/items")
def get_items(sort_by: str = 'item_id', order: str = 'ASC'):
    order = order.upper()
    if (sort_by not in sortables) or (order not in orderables):
        raise HTTPException(status_code=422)
    query_str = f"""
    SELECT * FROM items
    ORDER BY {identifier(sort_by)} {order};
    """
    db = connect_to_db()
    result = db.run(query_str)
    close_db_connection(db)
    sorted_list = sort_them_into_list(result, db.columns)
    return sorted_list


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=404)
    query_str = """
    SELECT * FROM items
    WHERE item_id = :item_id;
    """
    db = connect_to_db()
    result = db.run(query_str, item_id=item_id)
    close_db_connection(db)
    if len(result) == 0:
        raise HTTPException(status_code=404)
    sorted_dict = sort_it_into_dict(result[0], db.columns)
    return sorted_dict

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=404)
    query_str = """
    DELETE FROM items
    WHERE item_id = :item_id
    RETURNING *;
    """
    db = connect_to_db()
    result = db.run(query_str, item_id=item_id)
    close_db_connection(db)
    if len(result) == 0:
        raise HTTPException(status_code=404)
    # sorted_dict = sort_it_into_dict(result[0], db.columns)
    # return sorted_dict