"""
Avvio del server FastAPI.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Massimo AI backend attivo"}
