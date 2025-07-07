# database/connection.py
"""
CONNESSIONE DB – SQLAlchemy per Massimo AI
Gestione engine, session, pooling e sicurezza.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import Config

engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
