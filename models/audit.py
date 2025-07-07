# models/audit.py
"""
AUDIT – Audit trail, versioning e log storico Massimo AI

- Log di ogni modifica/azione su oggetti chiave
- Pronto per GDPR/AI Act
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import datetime

class AuditLog(BaseModel):
    id: int = Field(..., description="ID audit")
    object_type: str = Field(..., description="Tipo oggetto (user, agent, world, ...)")
    object_id: int = Field(..., description="ID oggetto")
    action: str = Field(..., description="Azione eseguita")
    user_id: Optional[int] = Field(None, description="Chi ha fatto l’azione")
    details: Optional[Dict[str, Any]] = Field(default_factory=dict)
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

    class Config:
        orm_mode = True
