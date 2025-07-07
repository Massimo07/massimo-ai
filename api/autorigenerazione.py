# /backend/api/autorigenerazione.py

from fastapi import APIRouter, Request
from autorigenerazione_ai.ecosystem_manager import AutorigenerazioneManager

router = APIRouter()
manager = AutorigenerazioneManager()

@router.post("/ai/autorigenerazione/suggerisci")
async def suggerisci_upgrade(request: Request):
    data = await request.json()
    user_level = data.get("user_level")
    context = data.get("context", {})
    return manager.suggerisci_upgrade(user_level, context)

@router.post("/ai/autorigenerazione/esegui")
async def esegui_autoupgrade(request: Request):
    data = await request.json()
    user_level = data.get("user_level")
    context = data.get("context", {})
    return manager.esegui_autoupgrade(user_level, context)
