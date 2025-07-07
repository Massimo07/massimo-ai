from fastapi import APIRouter, HTTPException
from backend.onboarding_module import USERS, SPONSORS

router = APIRouter()

BASE_URL = "http://127.0.0.1:8000/onboarding/registrazione"

# Crea link referral unico per ogni sponsor
@router.get("/referral/genera", tags=["Referral"])
def genera_referral(sponsor_id: int):
    """Genera un link referral unico per uno sponsor."""
    sponsor = next((s for s in SPONSORS if s["id"] == sponsor_id), None)
    if not sponsor:
        raise HTTPException(status_code=404, detail="Sponsor non trovato")
    referral_link = f"{BASE_URL}?sponsor_id={sponsor_id}"
    return {"sponsor": sponsor["nome"], "referral_link": referral_link}

# Visualizza iscritti per sponsor (referral tracking)
@router.get("/referral/iscritti", tags=["Referral"])
def iscritti_sponsor(sponsor_id: int):
    """Mostra tutti gli utenti iscritti con uno specifico sponsor."""
    sponsor = next((s for s in SPONSORS if s["id"] == sponsor_id), None)
    if not sponsor:
        raise HTTPException(status_code=404, detail="Sponsor non trovato")
    iscritti = [u for u in USERS if u["sponsor_id"] == sponsor_id]
    return {
        "sponsor": sponsor["nome"],
        "totale_iscritti": len(iscritti),
        "iscritti": iscritti
    }

# Visualizza tutti i referral attivi
@router.get("/referral/tutti", tags=["Referral"])
def tutti_referral():
    """Ritorna tutti i referral/sponsor con totale iscritti."""
    lista = []
    for s in SPONSORS:
        count = sum(1 for u in USERS if u["sponsor_id"] == s["id"])
        lista.append({"sponsor": s["nome"], "referral": f"{BASE_URL}?sponsor_id={s['id']}", "iscritti": count})
    return lista
