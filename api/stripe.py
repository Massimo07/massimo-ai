# api/stripe.py
"""
STRIPE API – Gestione pagamenti Stripe, webhook, audit (Massimo AI)

- Endpoint: POST /stripe/payment, POST /stripe/webhook
- Logging di ogni pagamento e evento webhook
"""

from fastapi import APIRouter, Request
from typing import Dict
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("api.stripe")
logger.setLevel(logging.INFO)

_fake_stripe_payments = []

@router.post("/stripe/payment", tags=["stripe"])
def stripe_payment(pa_
