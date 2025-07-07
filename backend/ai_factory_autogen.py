from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from backend.mondi_factory_module import MONDI

router = APIRouter()

class AIWorldGenRequest(BaseModel):
    settore: str
    descrizione: Optional[str] = ""
    target: Optional[str] = "tutti"
    lingua: Optional[str] = "it"
    livelli: Optional[List[str]] = []
    ruoli: Optional[List[str]] = []

@router.post("/ai-factory/genera-mondo", tags=["AI Factory"])
def genera_mondo_ai(data: AIWorldGenRequest):
    # Generazione automatica (simulata – si può collegare anche OpenAI)
    nome = f"{data.settore.capitalize()} World"
    branding = f"🌍 {data.settore.upper()}"
    default_livelli = data.livelli or ["Base", "Avanzato", "Premium"]
    default_ruoli = data.ruoli or ["utente", "mentor", "admin"]
    mondo = {
        "nome": nome,
        "descrizione": data.descrizione or f"Piattaforma per {data.settore}",
        "branding": branding,
        "livelli": default_livelli,
        "ruoli": default_ruoli,
        "lingua": data.lingua,
        "target": data.target,
        "utenti": [],
        "creato_da_ai": True
    }
    # Controlla duplicati
    if any(m["nome"].lower() == nome.lower() for m in MONDI):
        raise HTTPException(status_code=400, detail="Mondo già esistente!")
    MONDI.append(mondo)
    return {
        "messaggio": f"Mondo '{nome}' generato da AI!",
        "mondo": mondo
    }
