from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from config.database import SessionLocal
from schemas.index import Assignment
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
