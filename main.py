import string
import random
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    mystr = ''.join(random.choices(string.ascii_lowercase, k = 5))
    return {'data': mystr}

@app.get('/items/{item_id}')
async def read(item_id: int):
    return {'item_id': item_id}