from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL='mysql+mysqlconnector://sk33jnnnpvcz37jm:e5m21wwv2e5ysgb6@spryrr1myu6oalwl.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/a0o2yx84w0seyiax'

SQLALCHEMY_DATABASE_URL='mysql+mysqlconnector://root@localhost:3306/employee'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()