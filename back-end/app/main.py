import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def hello(name: str, age: int):
    return {"name": name, "age": age}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
