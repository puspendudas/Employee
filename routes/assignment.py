from fastapi import APIRouter, Depends, responses, status, Response, HTTPException
from sqlalchemy.orm.session import Session
from config.database import SessionLocal, engine
from schemas.index import Assignment
from datetime import datetime
from components.index import add_ass

assignment = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@assignment.post('/assignment/', status_code=status.HTTP_201_CREATED)
def add_assignment(request: Assignment ,db: Session = Depends(get_db)):
    return add_ass(request,db)
