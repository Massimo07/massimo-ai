# api/endpoint/users.py
"""
ENDPOINT – USERS (Massimo AI)
REST API demo per utenti, logging, audit, explainability.
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("endpoint.users")
logger.setLevel(logging.INFO)

_fake_users = []

@router.get("/endpoint/users", tags=["endpoint-users"])
def list_users() -> List[Dict]:
    """
    Elenco utenti demo (logging, explain).
    """
    logger.info(f"[endpoint.users] Elenco utenti: {len(_fake_users)} totali")
    return _fake_users

@router.post("/endpoint/users", tags=["endpoint-users"])
def add_user(user: Dict) -> Dict:
    """
    Registra un utente (audit, explain).
    """
    user["id"] = len(_fake_users) + 1
    user["created_at"] = datetime.datetime.utcnow().isoformat()
    _fake_users.append(user)
    logger.info(f"[endpoint.users] Utente aggiunto: {user}")
    return {"status": "ok", "explain": "Utente registrato da endpoint demo."}
