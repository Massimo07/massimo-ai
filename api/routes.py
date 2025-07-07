# api/routes.py
"""
ROUTES API – Gestione dinamica delle rotte REST (Massimo AI)

- Endpoint: POST /routes/register, GET /routes
- Logging e explainability per ogni route
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("api.routes")
logger.setLevel(logging.INFO)

_fake_routes_db: List[Dict] = []

@router.post("/routes/register", tags=["routes"])
def register_route(route: Dict) -> Dict:
    """
    Registra una nuova rotta REST (audit, explain).
    """
    route["id"] = len(_fake_routes_db) + 1
    route["registered_at"] = datetime.datetime.utcnow().isoformat()
    _fake_routes_db.append(route)
    logger.info(f"[routes] Route registrata: {route}")
    return {"status": "ok", "explain": "Route registrata con successo."}

@router.get("/routes", tags=["routes"])
def list_routes() -> List[Dict]:
    """
    Elenco di tutte le rotte registrate.
    """
    logger.info(f"[routes] Elenco routes, totale: {len(_fake_routes_db)}")
    return _fake_routes_db
