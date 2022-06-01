from fastapi import FastAPI, Depends, responses, status, Response, HTTPException
from sqlalchemy.orm.session import Session
from config.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.index import stat, employee, task, assignment

Base.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stat, tags=['Status'])
app.include_router(employee, tags=['Employee'])
app.include_router(task, tags=['Task'])
app.include_router(assignment, tags=['Assignment'])
