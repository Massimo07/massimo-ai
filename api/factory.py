# api/factory.py
"""
FACTORY API – Generazione dinamica di mondi/istanze AI (Massimo AI)

- Endpoint: POST /factory, GET /factory
- Logging e explainability su ogni creazione
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("api.factory")
logger.setLevel(logging.INFO)

_fake_worlds_db: List[Dict] = []

@router.post("/factory", tags=["factory"])
def create_world(world: Dict) -> Dict:
    """
    Crea un nuovo mondo/istanza AI (audit, explain).
    """
    world["id"] = len(_fake_worlds_db) + 1
    world["created_at"] = datetime.datetime.utcnow().isoformat()
    _fake_worlds_db.append(world)
    logger.info(f"[factory] Nuovo mondo creato: {world}")
    return {"status": "ok", "explain": "Mondo AI generato con successo."}

@router.get("/factory", tags=["factory"])
def list_worlds() -> List[Dict]:
    """
    Restituisce tutte le istanze/mondi creati.
    """
    logger.info(f"[factory] Elenco mondi, totale: {len(_fake_worlds_db)}")
    return _fake_worlds_db
