from fastapi import FastAPI
from App.routers import Credentials

app = FastAPI(debug=True)


# Dependency function to get a new DB session
def get_sql_db_session():
    session = Credentials.sql_engine.connect()
    try:
        yield session
    finally:
        session.close()


def get_postgres_db_session():
    session = Credentials.postgres_engine.connect()
    try:
        yield session
    finally:
        session.close()
