# api/endpoint/automation.py
"""
ENDPOINT – AUTOMATION (Massimo AI)
REST API per automazioni/task scheduler (audit trail e explain).
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("endpoint.automation")
logger.setLevel(logging.INFO)

_fake_automation = []

@router.get("/endpoint/automation", tags=["endpoint-automation"])
def list_automations() -> List[Dict]:
    """
    Elenco automazioni registrate (demo, logging, explain).
    """
    logger.info(f"[endpoint.automation] Elenco automazioni: {len(_fake_automation)} totali")
    return _fake_automation

@router.post("/endpoint/automation", tags=["endpoint-automation"])
def add_automation(automation: Dict) -> Dict:
    """
    Aggiungi una nuova automazione (audit, explain).
    """
    automation["id"] = len(_fake_automation) + 1
    automation["created_at"] = datetime.datetime.utcnow().isoformat()
    _fake_automation.append(automation)
    logger.info(f"[endpoint.automation] Automazione aggiunta: {automation}")
    return {"status": "ok", "explain": "Automazione registrata."}
