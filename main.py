import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

def Machine(arr):
    # load the model from disk
    filename = "gnb-divorce.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(arr)
    return result

@app.get("/")
async def root():
    return {"message": "Hello World"}

class Item(BaseModel):
    input: list = []

@app.post("/machine")
async def get_value(item: Item):
    raw = [[]]
    for i in item.input:
        raw[0].append(int(i))
    data = np.array(raw)
    result = Machine(data)
    return {"value": int(result[0])}
