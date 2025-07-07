# api/event.py
"""
EVENT API – Log, audit e analisi eventi di sistema (Massimo AI)

- Endpoint: POST /event, GET /event
- Logging dettagliato e audit di ogni evento critico
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("api.event")
logger.setLevel(logging.INFO)

_fake_event_db: List[Dict] = []

@router.post("/event", tags=["event"])
def register_event(event: Dict) -> Dict:
    """
    Registra un evento di sistema/utente (audit trail, explain).
    """
    event["id"] = len(_fake_event_db) + 1
    event["timestamp"] = datetime.datetime.utcnow().isoformat()
    _fake_event_db.append(event)
    logger.info(f"[event] Evento registrato: {event}")
    return {"status": "ok", "explain": f"Evento di tipo '{event.get('type','sconosciuto')}' loggato."}

@router.get("/event", tags=["event"])
def list_events() -> List[Dict]:
    """
    Restituisce tutti gli eventi registrati.
    """
    logger.info(f"[event] Elenco eventi, totale: {len(_fake_event_db)}")
    return _fake_event_db
