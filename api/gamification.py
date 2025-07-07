# api/gamification.py
"""
GAMIFICATION API – Badge, ranking, reward (Massimo AI)

- Endpoint: POST /gamification, GET /gamification
- Logging e audit su badge/ranking
- Explainability motivata su reward
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime
import random

router = APIRouter()
logger = logging.getLogger("api.gamification")
logger.setLevel(logging.INFO)

_fake_badges_db: List[Dict] = []

@router.post("/gamification", tags=["gamification"])
def award_badge(badge: Dict) -> Dict:
    """
    Assegna badge/ranking a un utente (audit, explain).
    """
    badge["id"] = len(_fake_badges_db) + 1
    badge["awarded_at"] = datetime.datetime.utcnow().isoformat()
    badge["score"] = random.randint(1, 100)
    _fake_badges_db.append(badge)
    logger.info(f"[gamification] Badge assegnato: {badge}")
    return {"status": "ok", "explain": f"Badge '{badge.get('nome','?')}' assegnato con punteggio {badge['score']}"}

@router.get("/gamification", tags=["gamification"])
def list_badges() -> List[Dict]:
    """
    Restituisce tutti i badge assegnati.
    """
    logger.info(f"[gamification] Elenco badge, totale: {len(_fake_badges_db)}")
    return _fake_badges_db
