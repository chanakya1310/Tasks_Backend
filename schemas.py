from typing import List, Optional
from pydantic import BaseModel

class TaskCreate(BaseModel):
    task_name : str
    task_description : str

class Task(TaskCreate):
    id : int

    class Config:
        orm_mode = True
