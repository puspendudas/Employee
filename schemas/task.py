from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Task(BaseModel):
    tsk_name : str
    tsk_designation : str