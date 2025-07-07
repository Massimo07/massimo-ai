from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from backend.branding_module import crea_branding, BrandingRequest

router = APIRouter()

SETTORE_DOMANDE = {
    "wellness": [
        "Qual è il tuo obiettivo di benessere?",
        "Hai già praticato tecniche di wellness?",
        "Quanto tempo vuoi dedicare ogni giorno?"
    ],
    "arte": [
        "Che tipo di arte preferisci?",
        "Vorresti condividere le tue opere?",
        "Ti piacerebbe partecipare a mostre/eventi?"
    ],
    "business": [
        "Hai già esperienza imprenditoriale?",
        "Cosa vuoi ottenere con questa piattaforma?",
        "Quanto vuoi investire in formazione personale?"
    ],
    "default": [
        "Qual è la tua motivazione principale?",
        "Cosa ti aspetti dal mondo {nome}?",
        "Come possiamo aiutarti al meglio?"
    ]
}

class OnboardingSmartRequest(BaseModel):
    settore: str
    target: Optional[str] = "tutti"
    lingua: Optional[str] = "it"
    valore: Optional[str] = "crescita"

@router.post("/onboarding-smart/genera", tags=["Onboarding Smart"])
def onboarding_smart(data: OnboardingSmartRequest):
    # Genera branding automatico
    branding = crea_branding(BrandingRequest(**data.dict()))
    # Domande personalizzate per settore
    domande = SETTORE_DOMANDE.get(data.settore.lower(), SETTORE_DOMANDE["default"])
    domande = [d.replace("{nome}", branding["nome_mondo"]) for d in domande]
    # Adattamento lingua semplificato (espandibile)
    if data.lingua == "en":
        domande = [d.replace("Qual è", "What is").replace("Cosa", "What").replace("Come", "How") for d in domande]
        branding["claim"] = f"[EN] {branding['claim']}"
    return {
        "mondo": branding["nome_mondo"],
        "claim": branding["claim"],
        "palette": branding["palette"],
        "icona": branding["icona"],
        "domande_onboarding": domande
    }
