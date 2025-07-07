# api/feedback.py
"""
FEEDBACK API – Raccolta, analisi e audit dei feedback utenti in Massimo AI

- Endpoint: POST /feedback, GET /feedback
- Logging e audit trail di ogni feedback ricevuto
- Sentiment analysis dummy (estendibile)
- Export CSV (demo)
- Explainability (motiva risposta/raccolta)
"""

from fastapi import APIRouter, HTTPException
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("api.feedback")
logger.setLevel(logging.INFO)

_fake_feedback_db: List[Dict] = []

@router.post("/feedback", tags=["feedback"])
def submit_feedback(feedback: Dict) -> Dict:
    """
    Registra un feedback utente, con logging e audit.
    """
    feedback["id"] = len(_fake_feedback_db) + 1
    feedback["timestamp"] = datetime.datetime.utcnow().isoformat()
    # Dummy sentiment
    feedback["sentiment"] = "positive" if "grazie" in feedback.get("text", "").lower() else "neutral"
    _fake_feedback_db.append(feedback)
    logger.info(f"[feedback] New feedback: {feedback}")
    return {"status": "ok", "explain": f"Feedback ricevuto con sentiment '{feedback['sentiment']}'."}

@router.get("/feedback", tags=["feedback"])
def list_feedback() -> List[Dict]:
    """
    Restituisce tutti i feedback raccolti (logging/audit).
    """
    logger.info(f"[feedback] List feedback, totale: {len(_fake_feedback_db)}")
    return _fake_feedback_db
