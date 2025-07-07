# database/models.py
"""
MODELLI ORM – SQLAlchemy (o altro ORM) per Massimo AI

Definizione tabelle utenti, mondi, agenti, abbonamenti, feedback.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String, unique=True)
    status = Column(String, default="attivo")
    provincia = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Altri modelli: World, Agent, Subscription, Feedback... (puoi copiarli dal core/models.py e adattarli)

