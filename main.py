from fastapi import FastAPI, Path , Query
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
def store(item_id : int = Path( description= "The ID of the item you want to get ")):
    if not biedronka[item]:
        return {"Error": "Item not found"}
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

@app.put("/update-item/{item_id}")
def update_item(item_id:int, item :UpdateItem):
    if item_id not in biedronka:
        return {"Error" : "Item does not exist in Biedronka"}

    if item.product is not None:
        biedronka[item_id].product = item.product

    if item.price is not None:
        biedronka[item_id].price = item.price

    if item.brand is not None:
        biedronka[item_id].brand = item.brand

    if item.quantity is not None:
        biedronka[item_id].quantity = item.quantity
        
    return biedronka[item_id]

@app.delete("/delete-item")
def delete_item (item_id : int = Query(..., description= "The ID of the item to DELETE" , gt=0)):
    if item_id not in biedronka:
        return {"Error" : "The ID does not exist"}
    deleted_item = biedronka.pop(item_id)
    return {"Success" : "Item deleted !" , "Deleted_Item " : deleted_item}


