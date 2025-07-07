from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.onboarding_module import USERS

router = APIRouter()

# Finto database livelli (può diventare DB reale)
LIVELLI = [
    {"id": 0, "nome": "Info Free", "prezzo": 0, "desc": "Accesso base gratuito"},
    {"id": 1, "nome": "Primo Passo", "prezzo": 15, "desc": "Inizia il tuo percorso"},
    {"id": 2, "nome": "Cambio Vita", "prezzo": 40, "desc": "Trasforma la tua mentalità"},
    {"id": 3, "nome": "Mentalità Vincente", "prezzo": 70, "desc": "Allenamento avanzato"},
    {"id": 4, "nome": "Crescita Esponenziale", "prezzo": 110, "desc": "Cresci senza limiti"},
    {"id": 5, "nome": "Imprenditore Libero", "prezzo": 160, "desc": "Libertà totale"},
    {"id": 6, "nome": "Guida del Team", "prezzo": 220, "desc": "Diventa leader del gruppo"},
    {"id": 7, "nome": "Network Leggendario", "prezzo": 300, "desc": "La vetta assoluta!"},
]

# Aggancia il livello all’utente (in memoria)
class LivelloUpdate(BaseModel):
    email: str
    livello_id: int

@router.get("/livelli", tags=["Livelli"])
def get_livelli():
    """Mostra tutti i livelli disponibili."""
    return LIVELLI

@router.post("/livelli/upgrade", tags=["Livelli"])
def upgrade_livello(data: LivelloUpdate):
    """Aggiorna il livello di un utente (collega a memoria)."""
    user = next((u for u in USERS if u["email"] == data.email), None)
    livello = next((l for l in LIVELLI if l["id"] == data.livello_id), None)
    if not user or not livello:
        raise HTTPException(status_code=404, detail="Utente o livello non trovato")
    user["livello"] = livello["nome"]
    return {"email": data.email, "nuovo_livello": livello}

@router.get("/livelli/utente", tags=["Livelli"])
def get_livello_utente(email: str):
    """Mostra il livello attuale di un utente."""
    user = next((u for u in USERS if u["email"] == email), None)
    if not user:
        raise HTTPException(status_code=404, detail="Utente non trovato")
    return {"email": email, "livello": user.get("livello", "Info Free")}
