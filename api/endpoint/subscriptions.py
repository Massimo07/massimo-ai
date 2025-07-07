# api/endpoint/subscriptions.py
"""
ENDPOINT – SUBSCRIPTIONS (Massimo AI)
REST API demo abbonamenti, logging e audit explainability.
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("endpoint.subscriptions")
logger.setLevel(logging.INFO)

_fake_subscriptions = []

@router.get("/endpoint/subscriptions", tags=["endpoint-subscriptions"])
def list_subscriptions() -> List[Dict]:
    """
    Elenco abbonamenti demo (logging, explain).
    """
    logger.info(f"[endpoint.subscriptions] Elenco abbonamenti: {len(_fake_subscriptions)} totali")
    return _fake_subscriptions

@router.post("/endpoint/subscriptions", tags=["endpoint-subscriptions"])
def add_subscription(sub: Dict) -> Dict:
    """
    Registra un abbonamento (audit, explain).
    """
    sub["id"] = len(_fake_subscriptions) + 1
    sub["created_at"] = datetime.datetime.utcnow().isoformat()
    _fake_subscriptions.append(sub)
    logger.info(f"[endpoint.subscriptions] Abbonamento registrato: {sub}")
    return {"status": "ok", "explain": "Abbonamento registrato da endpoint demo."}
