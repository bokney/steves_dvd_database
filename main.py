from db.connection import connect_to_db, close_db_connection
from fastapi import FastAPI
from pydantic import BaseModel
from util import sort_it_into_dict

app = FastAPI()

@app.get("/")
def read_root() -> str:
    return "server is running ✅"

class Item(BaseModel):
    name: str
    description: str
    
@app.post("/items")
def create_item(item: Item):
    query_str = """
    INSERT INTO items (name, description)
    VALUES (:name, :description)
    RETURNING *;        
    """
    db = connect_to_db()
    result = db.run(query_str, name=item.name, description=item.description)
    close_db_connection(db)
    sorted_dict = sort_it_into_dict(result[0], db.columns)
    return sorted_dict

@app.get("/items/{item_id}")
def get_item(item_id):
    query_str = """
    SELECT * FROM items
    WHERE item_id = :item_id;
    """
    db = connect_to_db()
    result = db.run(query_str, item_id=item_id)
    close_db_connection(db)
    sorted_dict = sort_it_into_dict(result[0], db.columns)
    return sorted_dict