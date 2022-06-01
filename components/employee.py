from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from models.index import DbTask, DbAssignment, DbEmployee
from config.database import SessionLocal, engine
from datetime import datetime
from schemas.index import Employee

category = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_emp(request: Employee, db: Session = Depends(get_db)):
    emp = DbEmployee(
        emp_name = request.emp_name,
        emp_designation = request.emp_designation
    )
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return {'status': 'Success', 'details': 'Employee Added Successfully'}