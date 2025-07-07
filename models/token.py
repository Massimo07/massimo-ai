# models/token.py
"""
TOKEN – Gestione token, JWT, refresh, ACL Massimo AI

- Validità, ruoli, device, audit
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import datetime

class Token(BaseModel):
    id: int = Field(..., description="ID token")
    user_id: int = Field(..., description="ID utente")
    token: str = Field(..., description="Token JWT")
    scope: str = Field("basic", description="Scope/ruoli")
    expires_at: datetime.datetime = Field(..., description="Scadenza")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    ip: Optional[str] = Field(None, description="IP generazione")
    device: Optional[str] = Field(None, description="Device")
    audit: Optional[Dict[str, Any]] = Field(default_factory=dict)

    class Config:
        orm_mode = True
