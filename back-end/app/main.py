import uvicorn
from fastapi import FastAPI
import database
from database import add_module

app = FastAPI()


@app.get("/classes/")
def index():
    return database.print_classes()


@app.get("/hello/{name}")
async def hello(name: str, age: int):
    return {"name": name, "age": age}


@app.post("/items/")
async def insert_module(item: dict):
    add_module(item)
    return item


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
