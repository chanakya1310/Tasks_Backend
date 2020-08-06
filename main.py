from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@app.post("/tasks", response_model = schemas.Task)
def create_task(task : schemas.TaskCreate, db : Session = Depends(get_db)):
    return crud.create_task(db = db, task = task)

@app.get("/tasks", response_model = List[schemas.Task])
def read_tasks(skip : int = 0, limit : int = 100, db : Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip = skip, limit = limit)
    return tasks

