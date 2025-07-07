"""
Payments API – Gestione pagamenti, Stripe/PayPal, logging, webhook, audit antifrode.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import logging

router = APIRouter()

class Payment(BaseModel):
    id: str
    user_id: str
    amount: float
    status: str
    provider: str

PAYMENTS = {}

def get_current_user():
    return {"user_id": "admin"}

@router.get("/", response_model=List[Payment])
def list_payments(skip: int = 0, limit: int = 100, user_id: Optional[str] = None, current=Depends(get_current_user)):
    payments = list(PAYMENTS.values())
    if user_id:
        payments = [p for p in payments if p.user_id == user_id]
    return payments[skip:skip+limit]

@router.post("/", response_model=Payment, status_code=status.HTTP_201_CREATED)
def create_payment(payment: Payment, current=Depends(get_current_user)):
    if payment.id in PAYMENTS:
        raise HTTPException(409, detail="Payment already exists")
    PAYMENTS[payment.id] = payment
    logging.info(f"[payments] Creato payment {payment.id} da {current['user_id']}")
    return payment

@router.get("/{payment_id}", response_model=Payment)
def get_payment(payment_id: str, current=Depends(get_current_user)):
    payment = PAYMENTS.get(payment_id)
    if not payment:
        raise HTTPException(404, detail="Payment not found")
    return payment

@router.post("/webhook", status_code=status.HTTP_200_OK)
def payment_webhook(payload: dict):
    # Log ricezione evento da Stripe/PayPal
    logging.info(f"[payments] Webhook ricezione: {payload}")
    return {"status": "received"}
