from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from config.database import SessionLocal
from components.index import show_satus

stat = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@stat.get('/status/', status_code=status.HTTP_200_OK)
def allstatus(db: Session = Depends(get_db)):
    return show_satus(db)
