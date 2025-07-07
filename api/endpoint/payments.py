# api/endpoint/payments.py
"""
ENDPOINT – PAYMENTS (Massimo AI)
REST API per gestione pagamenti, audit e explainability.
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("endpoint.payments")
logger.setLevel(logging.INFO)

_fake_payments = []

@router.get("/endpoint/payments", tags=["endpoint-payments"])
def list_payments() -> List[Dict]:
    """
    Elenco pagamenti ricevuti (demo, logging, explain).
    """
    logger.info(f"[endpoint.payments] Pagamenti elencati: {len(_fake_payments)} totali")
    return _fake_payments

@router.post("/endpoint/payments", tags=["endpoint-payments"])
def add_payment(payment: Dict) -> Dict:
    """
    Registra un pagamento (audit, explain).
    """
    payment["id"] = len(_fake_payments) + 1
    payment["created_at"] = datetime.datetime.utcnow().isoformat()
    _fake_payments.append(payment)
    logger.info(f"[endpoint.payments] Pagamento registrato: {payment}")
    return {"status": "ok", "explain": "Pagamento registrato da endpoint demo."}
