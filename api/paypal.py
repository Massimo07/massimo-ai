# api/paypal.py
"""
PAYPAL API – Gestione pagamenti PayPal, webhook, audit (Massimo AI)

- Endpoint: POST /paypal/payment, POST /paypal/webhook
- Logging e explainability su ogni pagamento/evento
"""

from fastapi import APIRouter, Request
from typing import Dict
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("api.paypal")
logger.setLevel(logging.INFO)

_fake_paypal_payments = []

@router.post("/paypal/payment", tags=["paypal"])
def paypal_payment(payment: Dict) -> Dict:
    """
    Registra un pagamento PayPal (demo, audit).
    """
    payment["id"] = len(_fake_paypal_payments) + 1
    payment["timestamp"] = datetime.datetime.utcnow().isoformat()
    _fake_paypal_payments.append(payment)
    logger.info(f"[paypal] Pagamento registrato: {payment}")
    return {"status": "ok", "explain": "Pagamento PayPal registrato."}

@router.post("/paypal/webhook", tags=["paypal"])
async def paypal_webhook(request: Request) -> Dict:
    """
    Riceve e logga un webhook PayPal (audit, explain).
    """
    payload = await request.json()
    logger.info(f"[paypal] Webhook ricevuto: {payload}")
    return {"status": "ok", "explain": "Webhook PayPal ricevuto e loggato."}
