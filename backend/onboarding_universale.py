from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Simula "mondi" creati (importa da mondi_factory_module se vuoi)
from backend.mondi_factory_module import MONDI

ONBOARDINGS = {}

class OnboardingRequest(BaseModel):
    mondo_nome: str
    email: str
    nome: str
    ruolo: str
    lingua: str = "it"
    età: Optional[int] = None
    sesso: Optional[str] = None
    preferenze: Optional[List[str]] = []
    quiz: Optional[List[str]] = []

@router.post("/onboarding-universale/start", tags=["Onboarding Universale"])
def start_onboarding(data: OnboardingRequest):
    # Trova mondo
    mondo = next((m for m in MONDI if m["nome"].lower() == data.mondo_nome.lower()), None)
    if not mondo:
        raise HTTPException(status_code=404, detail="Mondo non trovato")
    # Crea record onboarding
    onboarding = data.dict()
    ONBOARDINGS.setdefault(mondo["nome"], []).append(onboarding)
    # Logica smart: messaggio personalizzato
    msg = f"Benvenut* in {mondo['nome']}!"
    if data.lingua != "it":
        msg += f" (Lingua selezionata: {data.lingua})"
    if data.ruolo.lower() == "mentor":
        msg += " Grazie per ispirare la community!"
    if data.età and data.età < 18:
        msg += " Per i minori, percorso protetto e motivazionale."
    return {
        "messaggio": msg,
        "onboarding_completo": onboarding
    }

# Visualizza tutti gli utenti onboarded per un mondo
@router.get("/onboarding-universale/lista", tags=["Onboarding Universale"])
def lista_onboarding(mondo_nome: str):
    return ONBOARDINGS.get(mondo_nome, [])

# Cambia lingua (anche auto-suggerita)
@router.post("/onboarding-universale/lingua", tags=["Onboarding Universale"])
def cambia_lingua(mondo_nome: str, email: str, nuova_lingua: str):
    onboarding_list = ONBOARDINGS.get(mondo_nome, [])
    for onboard in onboarding_list:
        if onboard["email"] == email:
            onboard["lingua"] = nuova_lingua
            return {"ok": True, "messaggio": f"Language switched to {nuova_lingua}"}
    raise HTTPException(status_code=404, detail="Utente o mondo non trovato")
