from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .routers import Credentials

app = FastAPI(debug=True)


# Dependency function to get a new DB session
def get_db_session():
    session = Credentials.engine.connect()
    try:
        yield session
    finally:
        session.close()

