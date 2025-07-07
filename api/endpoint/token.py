# api/endpoint/token.py
"""
ENDPOINT – TOKEN (Massimo AI)
REST API demo per token/sessioni, blacklist e audit.
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime
import random

router = APIRouter()
logger = logging.getLogger("endpoint.token")
logger.setLevel(logging.INFO)

_fake_tokens = []
_fake_blacklist = []

@router.post("/endpoint/token", tags=["endpoint-token"])
def issue_token(data: Dict) -> Dict:
    """
    Genera un token demo e logga l’emissione (audit, explain).
    """
    token = f"tok_{random.randint(10000,99999)}"
    entry = {
        "token": token,
        "issued_at": datetime.datetime.utcnow().isoformat(),
        "user_id": data.get("user_id", None)
    }
    _fake_tokens.append(entry)
    logger.info(f"[endpoint.token] Token generato: {entry}")
    return {"status": "ok", "token": token}

@router.post("/endpoint/token/blacklist", tags=["endpoint-token"])
def blacklist_token(token: Dict) -> Dict:
    """
    Inserisce un token demo nella blacklist (audit, explain).
    """
    tkn = token.get("token")
    if tkn:
        _fake_blacklist.append(tkn)
        logger.info(f"[endpoint.token] Token blacklisted: {tkn}")
        return {"status": "ok", "explain": "Token inserito in blacklist."}
    return {"status": "error", "detail": "Token mancante."}
