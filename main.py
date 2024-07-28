from fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy as db
import urllib


class PaymentData(BaseModel):
    amount: int
    date: str
    count: int


# Database credentials
password_encoded = urllib.parse.quote_plus('wsdfghjkrtyh')
username = 'sxdcfvghjk'
server = 'wssdfghyjuk'
source_name = 'sdfghj'

app = FastAPI()

# SQLAlchemy engine setup
engine = db.create_engine(
    f'mssql+pyodbc://{username}:{password_encoded}@{server}/{source_name}?driver=ODBC+Driver+17+for+SQL+Server')


@app.on_event("startup")
async def startup_event():
    # Connect to the database at startup
    global engine
    engine.connect()


@app.on_event("shutdown")
async def shutdown_event():
    # Close the database connection on shutdown
    engine.dispose()


@app.get("/Future_data")
async def read_data():
    cmd = ('DECLARE @StartDate DATE = dateadd(day, 2, CAST(GETDATE() AS DATE));'
           'DECLARE @EndDate DATE = CAST(GETDATE() AS DATE); '
           'SELECT SUM(Amount),COUNT(Amount) ,CAST( RequestDate AS DATE)'
           'FROM [HamtaDb].[dbo].[PaymentRequests] '
           'WHERE [RequestDate] > @EndDate AND [RequestDate] <= @StartDate '
           'GROUP BY RequestDate '
           'ORDER BY RequestDate asc')

    with engine.connect() as connection:
        result = connection.execute(db.text(cmd))
        data_dicts = [PaymentData(amount=int(row[0]), date=str(row[2]), count=int(row[1])) for row in result]

    return data_dicts
