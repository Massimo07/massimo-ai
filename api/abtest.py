# api/abtest.py
"""
ABTEST API – Test A/B, gestione esperimenti e audit trail (Massimo AI)

- Endpoint: POST /abtest, GET /abtest
- Logging e audit trail di ogni test/esperimento
- Explainability: motivazione scelta variante
- Demo integrata per test
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime
import random

router = APIRouter()
logger = logging.getLogger("api.abtest")
logger.setLevel(logging.INFO)

_fake_abtest_db: List[Dict] = []

@router.post("/abtest", tags=["abtest"])
def create_abtest(test: Dict) -> Dict:
    """
    Registra un nuovo test A/B.
    Sceglie variante random e motiva la scelta.
    """
    test["id"] = len(_fake_abtest_db) + 1
    test["timestamp"] = datetime.datetime.utcnow().isoformat()
    test["variant"] = random.choice(["A", "B"])
    _fake_abtest_db.append(test)
    logger.info(f"[abtest] New AB Test: {test}")
    return {"status": "ok", "variant": test["variant"], "explain": f"Scelta variante '{test['variant']}' per test automatico."}

@router.get("/abtest", tags=["abtest"])
def list_abtest() -> List[Dict]:
    """
    Restituisce tutti gli AB test registrati.
    """
    logger.info(f"[abtest] List AB Tests, totale: {len(_fake_abtest_db)}")
    return _fake_abtest_db
