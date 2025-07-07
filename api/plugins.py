# api/plugins.py
"""
PLUGINS API – Gestione dinamica plug-in REST/AI (Massimo AI)

- Endpoint: POST /plugins/register
- Logging e explainability su registrazione plug-in
"""

from fastapi import APIRouter
from typing import Dict, List
import logging
import datetime

router = APIRouter()
logger = logging.getLogger("api.plugins")
logger.setLevel(logging.INFO)

_fake_plugins_db: List[Dict] = []

@router.post("/plugins/register", tags=["plugins"])
def register_plugin(plugin: Dict) -> Dict:
    """
    Registra un plug-in REST/AI (audit, logging).
    """
    plugin["id"] = len(_fake_plugins_db) + 1
    plugin["registered_at"] = datetime.datetime.utcnow().isoformat()
    _fake_plugins_db.append(plugin)
    logger.info(f"[plugins] Plug-in registrato: {plugin}")
    return {"status": "ok", "explain": "Plug-in registrato con successo."}
