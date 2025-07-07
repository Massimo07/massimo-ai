# api/endpoint/agents.py
"""
ENDPOINT – AGENTS (Massimo AI)
REST API per agenti AI: elenco, aggiunta, audit e explainability.
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("endpoint.agents")
logger.setLevel(logging.INFO)

_fake_agents = []

@router.get("/endpoint/agents", tags=["endpoint-agents"])
def list_agents() -> List[Dict]:
    """
    Restituisce tutti gli agenti AI registrati.
    """
    logger.info(f"[endpoint.agents] Elenco agenti: {len(_fake_agents)} totali")
    return _fake_agents

@router.post("/endpoint/agents", tags=["endpoint-agents"])
def add_agent(agent: Dict) -> Dict:
    """
    Aggiunge un nuovo agente AI (audit trail, explain).
    """
    agent["id"] = len(
