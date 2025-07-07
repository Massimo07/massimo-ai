from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Finto "database" in memoria
USERS = []
SPONSORS = [
    {"id": 1, "nome": "Massimo AI", "provincia": "Worldwide", "desc": "AI Fondatore"},
    {"id": 2, "nome": "Giulia Motiva", "provincia": "Roma", "desc": "Top Networker"},
    {"id": 3, "nome": "Alessandro Sprint", "provincia": "Milano", "desc": "Mentor Innovativo"},
    # Puoi aggiungere altri sponsor!
]

# Modelli
class UserRegistration(BaseModel):
    nome: str
    cognome: str
    email: str
    cellulare: str
    provincia: str
    ruolo: str  # "venditore" o "cliente"
    sponsor_id: int
    quiz_risposte: Optional[List[str]] = []

class SponsorOut(BaseModel):
    id: int
    nome: str
    provincia: str
    desc: str

# Endpoint lista sponsor filtrabile
@router.get("/onboarding/sponsor", response_model=List[SponsorOut], tags=["Onboarding"])
def lista_sponsor(provincia: Optional[str] = None):
    """Ritorna lista sponsor filtrabile per provincia."""
    if provincia:
        return [s for s in SPONSORS if provincia.lower() in s['provincia'].lower()]
    return SPONSORS

# Endpoint quiz (domande fisse, puoi estendere)
@router.get("/onboarding/quiz", tags=["Onboarding"])
def quiz():
    """Restituisce domande quiz motivazionale/conoscitivo."""
    return {
        "domande": [
            "Qual è la tua motivazione principale?",
            "Hai mai lavorato nel network marketing?",
            "Cosa vuoi ottenere con Massimo AI?"
        ]
    }

# Registrazione utente con quiz e sponsor
@router.post("/onboarding/registrazione", tags=["Onboarding"])
def registrazione_utente(user: UserRegistration):
    """Registra utente, memorizza dati, collega sponsor, risponde motivazionale."""
    # Controllo sponsor valido
    sponsor = next((s for s in SPONSORS if s["id"] == user.sponsor_id), None)
    if not sponsor:
        raise HTTPException(status_code=400, detail="Sponsor non valido")
    # Controllo email già presente
    if any(u["email"] == user.email for u in USERS):
        raise HTTPException(status_code=400, detail="Utente già registrato")
    USERS.append(user.dict())
    frase_motivazionale = (
        "Benvenuto/a in Massimo AI! "
        "Hai fatto il primo passo per rivoluzionare la tua vita. "
        "Il tuo sponsor sarà sempre al tuo fianco!"
    )
    return {
        "messaggio": frase_motivazionale,
        "nome": user.nome,
        "sponsor": sponsor["nome"],
        "prossimo_step": "Puoi ora scegliere il tuo livello o effettuare il pagamento con Stripe!"
    }
