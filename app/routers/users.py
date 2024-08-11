import sqlalchemy as db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from App.models import PaymentData, CustomerTotalRemain, WeeklyWage
from App.dependencies import get_sqldb_session, get_postgres_db_session
from App.routers.commands import future_settlements_cmd, customer_remain_cmd, weekly_wage_cmd

router = APIRouter()


@router.get("/Future-settlements", response_model=list[PaymentData], tags=['Services'])
async def read_sql_data(db_session: Session = Depends(get_sqldb_session)):
    # Connect to the database using SQLAlchemy engine
    result = db_session.execute(db.text(future_settlements_cmd))
    data_dicts = [PaymentData(amount=float(row[0]), date=str(row[2]), count=int(row[1])) for row in result]

    # Return the list of PaymentData objects as JSON response
    return data_dicts


@router.get("/CustomerTotalRemain", response_model=list[CustomerTotalRemain], tags=['Services'])
async def read_customer_remain_data(db_session: Session = Depends(get_postgres_db_session)):
    # Connect to the database using SQLAlchemy engine
    result = db_session.execute(db.text(customer_remain_cmd))
    data_dicts = [CustomerTotalRemain(
                        total_remain=float(row[0]), branch_id=int(row[1]), branch_name=str(row[2])) for row in result]

    # Return the list of CustomerTotalRemain objects as JSON response
    return data_dicts


@router.get("/WeeklyWage", response_model=list[WeeklyWage], tags=['Services'])
async def read_weekly_wage_data(db_session: Session = Depends(get_postgres_db_session)):
    # Connect to the database using SQLAlchemy engine
    result = db_session.execute(db.text(weekly_wage_cmd))
    data_dicts = [WeeklyWage(weekly_number=int(row[0]), total_interest=float(row[1]),
                             first_week_date=str(row[2])) for row in result]

    # Return the list of WeeklyWage objects as JSON response
    return data_dicts


