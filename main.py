from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    product: str
    price: float
    brand: Optional[str] = None
    quantity: Optional[int] = None

class UpdateItem(BaseModel):
    product: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None
    quantity: Optional[int] = None

app = FastAPI()


biedronka = {}


@app.get("/")
def home():
    return {"Data" : "Welcome to the page"}

@app.get("/store/{item_id}")
def store(item_id : int = Path( description= "The ID of the item you want to get ",gt= 0)):
    return biedronka[item_id]

@app.get("/get-by-name/{item_id}")
def get_by_name(item_id : int, name : Optional[str]= None ):
    for item_id in biedronka:
        if biedronka[item_id]['product'] == name:
            return biedronka[item_id]
    return {'Data' : 'Not Found'}


@app.post("/create-item/{item_id}")
def create_item(item_id : int, item : Item):
    if item_id in biedronka:
        return {"Error" : "Item already exists in Biedronka"}

    biedronka[item_id] = item
    return biedronka[item_id]

@app.put("/update-item/{item_id}"):
def update_item(item_id:int, item :UpdateItem):
    if item_id not in biedronka:
        return {"Error" : "Item does not exist in Biedronka"}
    biedronka[item_id].update(item)
    return biedronka[item_id]



