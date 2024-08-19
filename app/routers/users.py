import sqlalchemy as db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from App.models import PaymentData, CustomerTotalRemain, WeeklyWage, UsableCredit, Transactions, FinalCredit
from App.dependencies import get_sqldb_session, get_postgres_db_session
from App.routers.commands import (future_settlements_cmd, customer_remain_cmd, weekly_wage_cmd,
                                  daily_usable_credit_cmd, daily_transactions_cmd, daily_final_credit_cmd)

router = APIRouter()


@router.get("/Future-settlements", response_model=list[PaymentData], tags=['Services'])
async def read_sql_data(db_session: Session = Depends(get_sqldb_session)):
    result = db_session.execute(db.text(future_settlements_cmd))
    data_dicts = [PaymentData(amount=float(row[0]), date=str(row[2]), count=int(row[1])) for row in result]
    return data_dicts


@router.get("/CustomerTotalRemain", response_model=list[CustomerTotalRemain], tags=['Services'])
async def read_customer_remain_data(db_session: Session = Depends(get_postgres_db_session)):
    result = db_session.execute(db.text(customer_remain_cmd))
    data_dicts = [CustomerTotalRemain(
        total_remain=float(row[0]), branch_id=int(row[1]), branch_name=str(row[2])) for row in result]
    return data_dicts


@router.get("/WeeklyWage", response_model=list[WeeklyWage], tags=['Services'])
async def read_weekly_wage_data(db_session: Session = Depends(get_postgres_db_session)):
    result = db_session.execute(db.text(weekly_wage_cmd))
    data_dicts = [WeeklyWage(week_number=int(row[0]), total_interest=float(row[1]),
                             first_week_date=str(row[2])) for row in result]
    return data_dicts


@router.get("/DailyUsableCredit", response_model=list[UsableCredit], tags=['Services'])
async def read_daily_usable_credit_data(db_session: Session = Depends(get_postgres_db_session)):
    result = db_session.execute(db.text(daily_usable_credit_cmd))
    data_dicts = [UsableCredit(date=str(row[0]), branch_name=str(row[1]),
                               sum_credit=float(row[2])) for row in result]
    return data_dicts


@router.get("/DailyFinalCredit", response_model=list[FinalCredit], tags=['Services'])
async def read_daily_usable_credit_data(db_session: Session = Depends(get_postgres_db_session)):
    result = db_session.execute(db.text(daily_final_credit_cmd))
    data_dicts = [FinalCredit(branch_name=str(row[0]), final_credit=float(row[1]),
                              tr_ge_date=str(row[2])) for row in result]
    return data_dicts


@router.get("/DailyTransactions", response_model=list[Transactions], tags=['Services'])
async def read_daily_final_credit_data(db_session: Session = Depends(get_postgres_db_session)):
    result = db_session.execute(db.text(daily_transactions_cmd))
    data_dicts = [Transactions(branch_name=str(row[0]), is_a_purchase=bool(row[1]),
                               total_amount=float(row[2]), date=str(row[3]), stock_code=str(row[4])) for row in result]
    return data_dicts
