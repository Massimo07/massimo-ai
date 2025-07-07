# models/agent.py
"""
AGENT – Modello agente AI/umano Massimo AI

- Dati, skillset, owner, status
- Audit log training/azioni
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
import datetime

class Agent(BaseModel):
    id: int = Field(..., description="ID agente")
    nome: str = Field(..., description="Nome agente")
    owner_id: Optional[int] = Field(None, description="ID owner (utente o sistema)")
    skillset: List[str] = Field(default_factory=list, description="Competenze/abilità")
    stato: str = Field("attivo", description="Stato agente")
    tipo: str = Field("AI", description="Tipo agente (AI, umano)")
    meta: Optional[Dict[str, Any]] = Field(default_factory=dict)
    audit: Optional[Dict[str, Any]] = Field(default_factory=dict)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

    class Config:
        orm_mode = True
