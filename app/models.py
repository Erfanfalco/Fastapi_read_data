from pydantic import BaseModel


class PaymentData(BaseModel):
    amount: float
    date: str
    count: int


class CustomerTotalRemain(BaseModel):
    total_remain: float
    branch_id: int
    branch_name: str


class WeeklyWage(BaseModel):
    weekly_number: int
    total_interest: float
    first_week_date: str
