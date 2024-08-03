from pydantic import BaseModel


class PaymentData(BaseModel):
    amount: int
    date: str
    count: int

