# models/world.py
"""
WORLD – Modello mondi digitali Massimo AI

- Attributi custom, branding, owner
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import datetime

class World(BaseModel):
    id: int = Field(..., description="ID mondo")
    nome: str = Field(..., description="Nome mondo")
    owner_id: Optional[int] = Field(None, description="Owner")
    stato: str = Field("attivo", description="Stato mondo")
    branding: Optional[Dict[str, Any]] = Field(default_factory=dict)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    meta: Optional[Dict[str, Any]] = Field(default_factory=dict)
    audit: Optional[Dict[str, Any]] = Field(default_factory=dict)

    class Config:
        orm_mode = True
