from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from fastapi import UploadFile, File

class Assignment(BaseModel):
    emp_id: int
    tsk_id: int
    ass_date: date
    status: str