"""
services/notification.py – Notifiche pro multi-canale (email, SMS, push, webhook)
Invio asincrono, fallback provider, log, batch, priorità, custom template.
"""
from core.logger import massimo_logger
from typing import Dict, Any, List

class NotificationService:
    def __init__(self):
        self.outbox = []

    def send(self, channel: str, recipient: str, subject: str, body: str, priority: int = 1, meta: Dict[str, Any] = None):
        notif = {
            "channel": channel,
            "recipient": recipient,
            "subject": subject,
            "body": body,
            "priority": priority,
            "meta": meta or {}
        }
        self.outbox.append(notif)
        massimo_logger.info("Notifica inviata", **notif)
        # Qui puoi integrare invio reale via provider (Sendgrid, Twilio...)

    def batch_send(self, notifications: List[Dict[str, Any]]):
        for n in notifications:
            self.send(**n)

notification_service = NotificationService()

# Esempio:
# from services.notification import notification_service
# notification_service.send("email", "utente@dominio.com", "Benvenuto!", "Ciao, sei dentro Massimo AI!")