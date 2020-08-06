from sqlalchemy.orm import Session

import models
import schemas

def create_task(db : Session, task : schemas.TaskCreate):
    db_task = models.Task(task_name = task.task_name, task_description = task.task_description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db : Session, skip : int = 0, limit : int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()