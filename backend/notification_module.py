import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
from backend.onboarding_module import USERS

router = APIRouter()
NOTIFICATION_LOG = []

class NotificationRequest(BaseModel):
    email: EmailStr
    oggetto: str
    messaggio: str

@router.post("/notifiche/invia", tags=["Notifiche"])
def invia_notifica(data: NotificationRequest):
    """Invia (simula) una notifica email a un utente e logga l’evento."""
    user = next((u for u in USERS if u["email"] == data.email), None)
    if not user:
        raise HTTPException(status_code=404, detail="Utente non trovato")
    log_entry = {
        "email": data.email,
        "oggetto": data.oggetto,
        "messaggio": data.messaggio
    }
    NOTIFICATION_LOG.append(log_entry)
    logging.info(f"Notifica inviata a {data.email}: {data.oggetto}")
    # Qui puoi collegare un vero invio email (SMTP/Sendgrid/Mailgun)
    return {"success": True, "detail": "Notifica simulata (o inviata)", "log": log_entry}

# Automazione: invio reminder onboarding a tutti
@router.post("/automazione/reminder-onboarding", tags=["Automazioni"])
def reminder_onboarding(messaggio: Optional[str] = None):
    """Invia reminder a tutti gli utenti registrati (simulato, loggato)."""
    log = []
    base_msg = messaggio or "Ricordati di completare il tuo percorso Massimo AI per ottenere tutti i benefici!"
    for u in USERS:
        entry = {
            "email": u["email"],
            "oggetto": "Reminder Massimo AI",
            "messaggio": base_msg
        }
        NOTIFICATION_LOG.append(entry)
        log.append(entry)
        logging.info(f"Reminder inviato a {u['email']}")
    return {"reminder_inviati": len(log), "log": log}

# Endpoint per vedere log notifiche/automazioni
@router.get("/notifiche/log", tags=["Notifiche"])
def notifiche_log():
    """Visualizza tutte le notifiche inviate/automatizzate."""
    return NOTIFICATION_LOG
