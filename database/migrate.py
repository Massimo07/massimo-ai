# database/migrate.py
"""
MIGRATE – Script rapido di migrazione/setup DB (Massimo AI)
Crea tutte le tabelle se non esistono.
"""

from database.connection import engine
from database.models import Base

def migrate():
    Base.metadata.create_all(bind=engine)
    print("Tabelle create/migrate OK.")

if __name__ == "__main__":
    migrate()
