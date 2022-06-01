from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class DbTask(Base):
    __tablename__ = 'task'
    tsk_id = Column(Integer, primary_key=True, autoincrement=True)
    tsk_name = Column(String(255), default=0, nullable=False)
    tsk_designation = Column(String(255), default=0, nullable=False)