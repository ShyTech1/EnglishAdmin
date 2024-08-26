import uvicorn
from fastapi import FastAPI
import database
from database import add_module
from fastapi.middleware.cors import CORSMiddleware
from database import get_db


app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.post("/modules/")
def create_modules(modules: List[ModuleCreate], db: Session = Depends(get_db)):
    db_modules = [Module_1(student_id=module.student_id, module_name=module.module_name) for module in modules]
    db.add_all(db_modules)
    db.commit()
    return {"status": "Modules created successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
