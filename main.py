from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    product: str
    price: float
    brand: Optional[str] = None
    quantity: Optional[int] = None

app = FastAPI()


biedronka = {
    1 : 
    { 
        'product' : 'coke',
        'price' : 4.99,
        'brand' : 'polski',
        'quantity' : 6
    },
    2 :
    {
        'product' : 'chocolate',
        'price' : 2.99,
        'brand' : 'milka',
        'quantity' : 3
    }
}


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
        return {"Error" : "Item is already exist in Biedronka"}

    biedronka[item_id] = {'product': item.product, 'price' : item.price, 'brand':item.brand, 'quantity': item.quantity}
    return biedronka[item_id]



