from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define a Pydantic model for the POST request body
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World"}

# GET endpoint with path and query parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
