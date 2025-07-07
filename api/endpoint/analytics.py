# api/endpoint/analytics.py
"""
ENDPOINT – ANALYTICS (Massimo AI)
API REST per esportazione/monitoraggio dati, logging e explainability.
"""

from fastapi import APIRouter
from typing import Dict, List, Optional
import logging

router = APIRouter()
logger = logging.getLogger("endpoint.analytics")
logger.setLevel(logging.INFO)

_fake_analytics = [
    {"event": "access", "count": 150},
    {"event": "payment", "count": 77}
]

@router.get("/endpoint/analytics", tags=["endpoint-analytics"])
def get_analytics(event: Optional[str] = None) -> List[Dict]:
    """
    Esporta dati analytics filtrati per evento (audit, explain).
    """
    filtered = [x for x in _fake_analytics if not event or x["event"] == event]
    logger.info(f"[endpoint.analytics] Export analytics: {filtered}")
    return filtered
