"""
Definizione dei modelli dati.
"""

from pydantic import BaseModel

class UserRequest(BaseModel):
    message: str
