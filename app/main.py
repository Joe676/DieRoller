from typing import Union
from fastapi import FastAPI, HTTPException
from random import randint

app = FastAPI()
standard_dice = (2, 4, 6, 8, 10, 12, 20, 100)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health", status_code=200)
def read_health():
    return {"health": "good"}

@app.get("/roll/{die_size}")
def read_item(die_size: int):
    if die_size not in standard_dice:
        raise HTTPException(status_code=404, 
                            detail=f"The requested number is not a size of a standard die, try one of: {standard_dice}")
    r = randint(1, die_size)
    return {"die_size": die_size, "roll": r}