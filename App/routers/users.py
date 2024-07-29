import sqlalchemy as db
from sqlalchemy.orm import Session
from App.dependencies import get_db_session
from App.models import PaymentData
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/Future-settlements", response_model=list[PaymentData])
async def read_data(db_session: Session = Depends(get_db_session)):
    # SQL command string to be executed against the database
    cmd = ('DECLARE @StartDate DATE = dateadd(day, 2, CAST(GETDATE() AS DATE));'
           'DECLARE @EndDate DATE = CAST(GETDATE() AS DATE); '
           'SELECT SUM(Amount),COUNT(Amount) ,CAST( RequestDate AS DATE)'
           'FROM [HamtaDb].[dbo].[PaymentRequests] '
           'WHERE [RequestDate] > @EndDate AND [RequestDate] <= @StartDate '
           'GROUP BY RequestDate '
           'ORDER BY RequestDate asc')

    # Connect to the database using SQLAlchemy engine
    result = db_session.execute(db.text(cmd))
    data_dicts = [PaymentData(amount=int(row[0]), date=str(row[2]), count=int(row[1])) for row in result]

    # Return the list of PaymentData objects as JSON response
    return data_dicts
