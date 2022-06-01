from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from models.index import DbTask, DbAssignment, DbEmployee
from config.database import SessionLocal, engine
from datetime import datetime
from schemas.index import Employee, Task, Assignment

category = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_ass(request: Assignment, db: Session = Depends(get_db)):
    ass = DbAssignment(
        emp_id = request.emp_id,
        tsk_id = request.tsk_id,
        ass_date = request.ass_date,
        status = request.status
    )
    db.add(ass)
    db.commit()
    db.refresh(ass)
    return {'status': 'Success', 'details': 'Assignment Added Successfully'}