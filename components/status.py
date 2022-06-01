from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from models.index import DbTask, DbAssignment, DbEmployee
from config.database import SessionLocal, engine
from datetime import datetime

category = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def show_satus(db: Session = Depends(get_db)):
    customer = db.query(DbEmployee).all()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Employee is not available")
    else:
        return customer