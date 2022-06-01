from pydantic import BaseModel

class Task(BaseModel):
    tsk_name : str
    tsk_designation : str