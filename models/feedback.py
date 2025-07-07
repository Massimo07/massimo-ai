# models/feedback.py
"""
FEEDBACK – Modello feedback/NPS Massimo AI

- Rating, testo, sentiment, audit
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import datetime

class Feedback(BaseModel):
    id: int = Field(..., description="ID feedback")
    user_id: int = Field(..., description="ID utente")
    testo: str = Field(..., description="Testo feedback")
    rating: int = Field(..., description="Valutazione (1–5)")
    sentiment: Optional[str] = Field(None, description="Analisi sentiment")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    audit: Optional[Dict[str, Any]] = Field(default_factory=dict)

    class Config:
        orm_mode = True
