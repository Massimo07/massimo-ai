# models/event.py
"""
EVENT – Log eventi sistema Massimo AI

- Tipologia, origine, correlazione
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import datetime

class Event(BaseModel):
    id: int = Field(..., description="ID evento")
    tipo: str = Field(..., description="Tipo evento")
    user_id: Optional[int] = Field(None, description="User/owner collegato")
    details: Optional[Dict[str, Any]] = Field(default_factory=dict)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    meta: Optional[Dict[str, Any]] = Field(default_factory=dict)

    class Config:
        orm_mode = True
