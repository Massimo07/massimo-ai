# api/endpoint/worlds.py
"""
ENDPOINT – WORLDS (Massimo AI)
REST API demo mondi digitali, logging e explain.
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("endpoint.worlds")
logger.setLevel(logging.INFO)

_fake_worlds = []

@router.get("/endpoint/worlds", tags=["endpoint-worlds"])
def list_worlds() -> List[Dict]:
    """
    Elenco mondi demo (logging, explain).
    """
    logger.info(f"[endpoint.worlds] Elenco mondi: {len(_fake_worlds)} totali")
    return _fake_worlds

@router.post("/endpoint/worlds", tags=["endpoint-worlds"])
def add_world(world: Dict) -> Dict:
    """
    Registra un mondo (audit, explain).
    """
    world["id"] = len(_fake_worlds) + 1
    world["created_at"] = datetime.datetime.utcnow().isoformat()
    _fake_worlds.append(world)
    logger.info(f"[endpoint.worlds] Mondo aggiunto: {world}")
    return {"status": "ok", "explain": "Mondo registrato da endpoint demo."}
