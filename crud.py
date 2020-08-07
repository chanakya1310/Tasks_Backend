from sqlalchemy.orm import Session

import models
import schemas

def create_task(db : Session, task : schemas.TaskCreate):
    db_task = models.Task(task_name = task.task_name, task_description = task.task_description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def create_user(db : Session, user : schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email = user.email, hashed_password = fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_tasks(db : Session, skip : int = 0, limit : int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def get_task_by_id(db : Session, id : str):
    return db.query(models.Task).filter(models.Task.id == id).first() 

def create_user_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_item = models.Task(**task.dict(), owner_id = user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item