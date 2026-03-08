from fastapi import FastAPI, Path

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
def store(item_id : int = Path( description= "The ID of the item you want to get ",gt= 0, lt = 3)):
    return biedronka[item_id]


