from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from models.employee import DbEmployee
from models.task import DbTask


class DbAssignment(Base):
    __tablename__ = 'assignment'
    ass_id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey(DbEmployee.emp_id), nullable=False)
    tsk_id = Column(Integer, ForeignKey(DbTask.tsk_id), nullable=False)
    ass_date = Column(Date, default=0, nullable=False)
    status = Column(String(255), default=0, nullable=False)

    cust_id_constraint = relationship(
    "DbEmployee", cascade="all,delete", backref="assignment")
    
    trans_operator_id_constraint = relationship(
    "DbTask", cascade="all,delete", backref="assignment")