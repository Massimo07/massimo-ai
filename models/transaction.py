# models/transaction.py
"""
TRANSACTION – Transazioni e pagamenti Massimo AI

- Import/export pagamenti
- Multicurrency, gateway
- Audit completo
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import datetime

class Transaction(BaseModel):
    id: int = Field(..., description="ID transazione")
    user_id: int = Field(..., description="ID utente")
    amount: float = Field(..., description="Importo")
    currency: str = Field("EUR", description="Valuta")
    gateway: str = Field(..., description="Gateway (stripe, paypal, etc.)")
    status: str = Field("success", description="Stato transazione")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    receipt_url: Optional[str] = Field(None, description="URL ricevuta")
    audit: Optional[Dict[str, Any]] = Field(default_factory=dict)

    class Config:
        orm_mode = True
