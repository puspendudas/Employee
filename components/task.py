from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from models.index import DbTask, DbAssignment, DbEmployee
from config.database import SessionLocal, engine
from datetime import datetime
from schemas.index import Employee, Task

category = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_tsk(request: Task, db: Session = Depends(get_db)):
    tsk = DbTask(
        tsk_name = request.tsk_name,
        tsk_designation = request.tsk_designation
    )
    db.add(tsk)
    db.commit()
    db.refresh(tsk)
    return {'status': 'Success', 'details': 'Task Added Successfully'}