from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Todo, Base

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

class TodoCreate(BaseModel):
    title: str
    description: str

@app.post("/todos/", response_model=TodoCreate)
async def create_todo(todo: TodoCreate):
    db = SessionLocal()
    db_todo = Todo(
        title=todo.title,
        description=todo.description
    )
    
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    db.close()
    return db_todo


@app.get("/todos/", response_model=list[TodoCreate])
async def read_todos(skip: int=0, limit: int = 10):
    db = SessionLocal()
    todos = db.query(Todo).offset(skip).limit(limit).all()
    db.close()
    return todos