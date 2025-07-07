from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import random

router = APIRouter()

PALETTE = [
    {"nome": "Energia", "colori": ["#FF5722", "#FFC107", "#4CAF50"]},
    {"nome": "Sofisticato", "colori": ["#212121", "#FFD700", "#00BCD4"]},
    {"nome": "Futuro", "colori": ["#673AB7", "#00E5FF", "#E040FB"]},
    {"nome": "Naturale", "colori": ["#388E3C", "#FFF176", "#B2FF59"]},
    {"nome": "Universale", "colori": ["#009688", "#FFEB3B", "#607D8B"]}
]
ICONE = ["🌍", "🚀", "💡", "🌱", "🎯", "🧠", "✨", "🏆", "🤖", "🔥", "🌟"]

class BrandingRequest(BaseModel):
    settore: str
    target: Optional[str] = "tutti"
    lingua: Optional[str] = "it"
    valore: Optional[str] = "crescita"

@router.post("/branding/crea", tags=["Branding AI"])
def crea_branding(data: BrandingRequest):
    # Naming: combina settore, valore, icona
    icon = random.choice(ICONE)
    nome = f"{icon} {data.settore.capitalize()}X"
    claim = {
        "it": [
            f"Il futuro del {data.settore}, oggi.",
            f"Dove il {data.settore} diventa crescita.",
            f"Per ogni {data.target}, la soluzione migliore.",
            f"{data.settore.capitalize()} per chi vuole di più."
        ],
        "en": [
            f"The future of {data.settore} starts now.",
            f"{data.settore.capitalize()} for the next generation.",
            f"Where {data.target} meets excellence.",
            f"{data.settore.capitalize()} that empowers you."
        ]
    }
    claim_sel = random.choice(claim.get(data.lingua, claim["it"]))
    palette = random.choice(PALETTE)
    descr = f"{nome}: piattaforma dedicata a {data.settore}, pensata per {data.target}. Valore chiave: {data.valore}."
    return {
        "nome_mondo": nome,
        "claim": claim_sel,
        "palette": palette["colori"],
        "stile": palette["nome"],
        "icona": icon,
        "descrizione": descr
    }
