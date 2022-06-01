from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from models.index import DbAssignment
from config.database import SessionLocal
from schemas.index import Assignment

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