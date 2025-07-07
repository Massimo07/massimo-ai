# models/subscription.py
"""
SUBSCRIPTION – Modello abbonamento/livello Massimo AI

- Livelli, status, upgrade, audit
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import datetime

class Subscription(BaseModel):
    id: int = Field(..., description="ID abbonamento")
    user_id: int = Field(..., description="ID utente")
    livello: str = Field(..., description="Nome/step abbonamento")
    status: str = Field("attivo", description="Stato abbonamento")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    expires_at: Optional[datetime.datetime] = Field(None, description="Scadenza")
    audit: Optional[Dict[str, Any]] = Field(default_factory=dict)

    class Config:
        orm_mode = True
