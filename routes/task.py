from fastapi import APIRouter, Depends, responses, status, Response, HTTPException
from sqlalchemy.orm.session import Session
from config.database import SessionLocal, engine
from schemas.index import Task
from datetime import datetime
from components.index import add_emp, add_tsk

task = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@task.post('/task/', status_code=status.HTTP_201_CREATED)
def add_task(request: Task ,db: Session = Depends(get_db)):
    return add_tsk(request,db)
