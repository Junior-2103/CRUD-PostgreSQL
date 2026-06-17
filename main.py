import os

import bcrypt
from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

load_dotenv()

URL = os.getenv(
    "DATABASE_URL"
)  # postgresql://{ user_name }:{ password }@{ host }:{ port }/{ database }

if not URL:
    raise Exception("Not defined a DATABASE_URL variable ambient for database")

app = FastAPI()
engine = create_engine(URL)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(72))


Base.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"Message": "Hello World!"}
