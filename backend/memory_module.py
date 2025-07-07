from fastapi import APIRouter, HTTPException
from backend.onboarding_module import USERS
from typing import Dict, List

router = APIRouter()

# "Database" in RAM delle memorie/follow-up (può essere poi sostituito con DB vero)
MEMORY = {}

# Aggiungi evento/messaggio/memo personalizzato all’utente
@router.post("/memory/add-event", tags=["Memory"])
def add_event(email: str, evento: str, dettaglio: str):
    """Aggiunge evento o memoria evolutiva all’utente."""
    user = next((u for u in USERS if u["email"] == email), None)
    if not user:
        raise HTTPException(status_code=404, detail="Utente non trovato")
    MEMORY.setdefault(email, []).append({"evento": evento, "dettaglio": dettaglio})
    return {"success": True, "memoria": MEMORY[email]}

# Ottieni tutta la storia/memoria di un utente
@router.get("/memory/get", tags=["Memory"])
def get_memory(email: str):
    """Ritorna la memoria evolutiva (tutte le interazioni) dell’utente."""
    if email not in MEMORY:
        return {"memoria": []}
    return {"memoria": MEMORY[email]}

# Follow-up automatico: aggiunge un evento di follow-up a tutti
@router.post("/memory/followup-all", tags=["Memory"])
def followup_all(evento: str, dettaglio: str):
    """Aggiunge un evento follow-up a TUTTI gli utenti registrati."""
    for u in USERS:
        MEMORY.setdefault(u["email"], []).append({"evento": evento, "dettaglio": dettaglio})
    return {"done": True, "utenti": len(USERS)}

# Cerca utenti con almeno un evento specifico
@router.get("/memory/find-by-event", tags=["Memory"])
def find_by_event(evento: str):
    """Ritorna tutti gli utenti che hanno avuto un certo evento nella loro memoria."""
    result = []
    for email, eventi in MEMORY.items():
        if any(ev["evento"] == evento for ev in eventi):
            result.append(email)
    return {"utenti": result}
