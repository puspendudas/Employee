from pydantic import BaseModel
from datetime import date

class Assignment(BaseModel):
    emp_id: int
    tsk_id: int
    ass_date: date
    status: str