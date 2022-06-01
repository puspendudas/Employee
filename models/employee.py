from config.database import Base
from sqlalchemy import Column, Integer, String


class DbEmployee(Base):
    __tablename__ = 'employee'
    emp_id = Column(Integer, primary_key=True, autoincrement=True)
    emp_name = Column(String(255), default=0, nullable=False)
    emp_designation = Column(String(255), default=0, nullable=False)