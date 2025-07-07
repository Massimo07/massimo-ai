# api/invite.py
"""
INVITE API – Gestione referral/inviti e tracking (Massimo AI)

- Endpoint: POST /invite, GET /invite
- Logging/audit su ogni referral
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime
import random

router = APIRouter()
logger = logging.getLogger("api.invite")
logger.setLevel(logging.INFO)

_fake_invite_db: List[Dict] = []

@router.post("/invite", tags=["invite"])
def create_invite(invite: Dict) -> Dict:
    """
    Registra un referral/invito e assegna un codice.
    """
    invite["id"] = len(_fake_invite_db) + 1
    invite["created_at"] = datetime.datetime.utcnow().isoformat()
    invite["referral_code"] = f"REF{random.randint(1000,9999)}"
    _fake_invite_db.append(invite)
    logger.info(f"[invite] Nuovo referral: {invite}")
    return {"status": "ok", "referral_code": invite["referral_code"], "explain": "Referral creato correttamente."}

@router.get("/invite", tags=["invite"])
def list_invites() -> List[Dict]:
    """
    Restituisce tutti i referral/inviti creati.
    """
    logger.info(f"[invite] Elenco referral, totale: {len(_fake_invite_db)}")
    return _fake_invite_db
