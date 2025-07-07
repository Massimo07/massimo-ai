from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PaymentBase(BaseModel):
    user_id: str
    amount: float
    currency: str = "EUR"
    method: str
    status: str = "pending"

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    status: Optional[str]

class Payment(PaymentBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True
