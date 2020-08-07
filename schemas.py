from typing import List, Optional
from pydantic import BaseModel

class TaskCreate(BaseModel):
    task_name : str
    task_description : str

class Task(TaskCreate):
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id : int
    is_active : bool
    tasks: List[Task] = []

    class Config:
        orm_mode = True
