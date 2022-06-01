from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from fastapi import UploadFile, File

class Employee(BaseModel):
    emp_name : str
    emp_designation : str