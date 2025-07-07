from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

MONDI = []

class MondoCreate(BaseModel):
    nome: str
    descrizione: str
    branding: str
    ruoli: List[str] = ["member"]
    livelli: List[str] = []
    admin_email: str

@router.post("/mondi/crea", tags=["AI Factory"])
def crea_mondo(data: MondoCreate):
    """Crea un nuovo mondo/servizio AI personalizzato."""
    if any(m["nome"].lower() == data.nome.lower() for m in MONDI):
        raise HTTPException(status_code=400, detail="Mondo già esistente")
    mondo = data.dict()
    mondo["utenti"] = []
    MONDI.append(mondo)
    return {"messaggio": f"Mondo '{data.nome}' creato!", "mondo": mondo}

@router.get("/mondi", tags=["AI Factory"])
def lista_mondi():
    """Mostra tutti i mondi attivi."""
    return MONDI

# Aggiungi utente a un mondo
class MondoJoin(BaseModel):
    mondo_nome: str
    email: str
    ruolo: str = "member"

@router.post("/mondi/join", tags=["AI Factory"])
def join_mondo(data: MondoJoin):
    for m in MONDI:
        if m["nome"].lower() == data.mondo_nome.lower():
            m["utenti"].append({"email": data.email, "ruolo": data.ruolo})
            return {"messaggio": f"{data.email} aggiunto a {m['nome']} come {data.ruolo}."}
    raise HTTPException(status_code=404, detail="Mondo non trovato")
