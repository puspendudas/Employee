from fastapi import APIRouter, Depends, responses, status, Response, HTTPException
from sqlalchemy.orm.session import Session
from config.database import SessionLocal, engine
from schemas.index import Employee
from datetime import datetime
from components.index import add_emp

employee = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@employee.post('/employee/', status_code=status.HTTP_201_CREATED)
def add_employee(request: Employee ,db: Session = Depends(get_db)):
    return add_emp(request,db)
