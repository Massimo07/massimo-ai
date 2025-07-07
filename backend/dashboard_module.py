from fastapi import APIRouter, Query
from typing import List, Optional
from backend.onboarding_module import USERS, SPONSORS

router = APIRouter()

# Dashboard - lista utenti, filtrabile
@router.get("/dashboard/utenti", tags=["Dashboard"])
def dashboard_utenti(
    sponsor_id: Optional[int] = Query(None),
    provincia: Optional[str] = Query(None),
    ruolo: Optional[str] = Query(None)
):
    """Visualizza utenti, filtra per sponsor, provincia, ruolo."""
    utenti = USERS
    if sponsor_id:
        utenti = [u for u in utenti if u["sponsor_id"] == sponsor_id]
    if provincia:
        utenti = [u for u in utenti if provincia.lower() in u["provincia"].lower()]
    if ruolo:
        utenti = [u for u in utenti if ruolo.lower() == u["ruolo"].lower()]
    return utenti

# Statistiche sponsor: quanti iscritti ha ogni sponsor?
@router.get("/dashboard/sponsor", tags=["Dashboard"])
def dashboard_sponsor():
    """Statistiche iscritti per sponsor."""
    stats = []
    for s in SPONSORS:
        count = sum(1 for u in USERS if u["sponsor_id"] == s["id"])
        stats.append({"sponsor": s["nome"], "iscritti": count})
    return stats

# Statistiche livelli: quanti utenti hanno scelto ogni ruolo
@router.get("/dashboard/livelli", tags=["Dashboard"])
def dashboard_livelli():
    """Statistiche per ruolo/“livello”."""
    levels = {}
    for u in USERS:
        key = u["ruolo"].lower()
        levels[key] = levels.get(key, 0) + 1
    return levels
