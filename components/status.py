from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from models.index import DbTask, DbAssignment, DbEmployee
from config.database import SessionLocal, engine
from datetime import date, datetime, timedelta


category = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def show_satus(db: Session = Depends(get_db)):


    
    today = db.query(DbAssignment, DbEmployee).join(DbEmployee).join(DbTask).filter(DbAssignment.ass_date == date.today()).filter(DbAssignment.status == "done").all()
    week = db.query(DbAssignment, DbEmployee).join(DbEmployee).join(DbTask).filter(DbAssignment.ass_date > date.today() - timedelta(weeks=1)).filter(DbAssignment.status == "done").all()
    month = db.query(DbAssignment, DbEmployee).join(DbEmployee).join(DbTask).filter(DbAssignment.ass_date > date.today() - timedelta(days=30)).filter(DbAssignment.status == "done").all()
    

    data_today = most_frequent(today)
    data_week = most_frequent(week)
    data_month = most_frequent(month)

    return {'Today': {'Employee Name': data_today.DbEmployee.emp_name, 'Employee Designation': data_today.DbEmployee.emp_designation, 'Employee Id': data_today.DbEmployee.emp_id ,'details': 'Employee of the day'},
            'Week': {'Employee Name': data_week.DbEmployee.emp_name, 'Employee Designation': data_week.DbEmployee.emp_designation, 'Employee Id': data_week.DbEmployee.emp_id ,'details': 'Employee of the week'},
            'Month': {'Employee Name': data_month.DbEmployee.emp_name, 'Employee Designation': data_month.DbEmployee.emp_designation, 'Employee Id': data_month.DbEmployee.emp_id ,'details': 'Employee of the month'}}


def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num