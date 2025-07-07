# api/payments/stripe_payment.py
"""
PAYMENTS – STRIPE (Massimo AI)
Gestione pagamenti Stripe, logging, audit, explainability.

- Endpoint: POST /payments/stripe, GET /payments/stripe
- Audit e log su ogni transazione Stripe demo
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("payments.stripe")
logger.setLevel(logging.INFO)

_fake_stripe_db: List[Dict] = []

@router.post("/payments/stripe", tags=["payments-stripe"])
def stripe_payment(payment: Dict) -> Dict:
    """
    Registra un pagamento Stripe (audit, explain).
    """
    payment["id"] = len(_fake_stripe_db) + 1
    payment["timestamp"] = datetime.datetime.utcnow().isoformat()
    _fake_stripe_db.append(payment)
    logger.info(f"[payments.stripe] Pagamento registrato: {payment}")
    return {"status": "ok", "explain": "Pagamento Stripe demo registrato."}

@router.get("/payments/stripe", tags=["payments-stripe"])
def list_stripe_payments() -> List[Dict]:
    """
    Elenco pagamenti Stripe demo (logging, explain).
    """
    logger.info(f"[payments.stripe] Elenco pagamenti: {len(_fake_stripe_db)} totali")
    return _fake_stripe_db
