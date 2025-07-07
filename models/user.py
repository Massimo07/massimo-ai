
---

## **models/user.py**

```python
# models/user.py
"""
USER – Modello utente Massimo AI

- Validato Pydantic
- Pronto per ORM
- Audit e versioning
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict, Any
import datetime

class User(BaseModel):
    id: int = Field(..., description="ID utente")
    nome: str = Field(..., description="Nome completo")
    email: EmailStr = Field(..., description="Email utente")
    status: str = Field("attivo", description="Stato account")
    ruolo: str = Field("user", description="Ruolo utente (admin, user, founder, AI, ecc.)")
    provincia: Optional[str] = Field(None, description="Provincia residenza")
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    meta: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Meta extra")
    audit: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Audit/versioning")

    class Config:
        orm_mode = True
