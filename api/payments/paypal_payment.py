# api/payments/paypal_payment.py
"""
PAYMENTS – PAYPAL (Massimo AI)
Gestione pagamenti PayPal, logging, audit, explainability.

- Endpoint: POST /payments/paypal, GET /payments/paypal
- Audit e log su ogni transazione PayPal demo
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("payments.paypal")
logger.setLevel(logging.INFO)

_fake_paypal_db: List[Dict] = []

@router.post("/payments/paypal", tags=["payments-paypal"])
def paypal_payment(payment: Dict) -> Dict:
    """
    Registra un pagamento PayPal (audit, explain).
    """
    payment["id"] = len(_fake_paypal_db) + 1
    payment["timestamp"] = datetime.datetime.utcnow().isoformat()
    _fake_paypal_db.append(payment)
    logger.info(f"[payments.paypal] Pagamento registrato: {payment}")
    return {"status": "ok", "explain": "Pagamento PayPal demo registrato."}

@router.get("/payments/paypal", tags=["payments-paypal"])
def list_paypal_payments() -> List[Dict]:
    """
    Elenco pagamenti PayPal demo (logging, explain).
    """
    logger.info(f"[payments.paypal] Elenco pagamenti: {len(_fake_paypal_db)} totali")
    return _fake_paypal_db
