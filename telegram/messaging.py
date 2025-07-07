"""
Modulo: messaging.py
Motore messaggi centralizzato per Massimo AI: invio, formattazione, personalizzazione, broadcast.
Supporta template dinamici, multilingua, variabili personalizzate, invio massivo su Telegram/WhatsApp/email.
"""

import logging
from notifications import send_notification

logger = logging.getLogger(__name__)

TEMPLATES = {
    "welcome": "Ciao {name}, benvenuto in Massimo AI! Pronto a scoprire il tuo potenziale?",
    "promo": "Non perdere la promo del mese: {promo}! Approfitta ora.",
    "badge": "Congratulazioni {name}, hai sbloccato il badge: {badge}!"
}

def render_template(key, **kwargs):
    template = TEMPLATES.get(key, "")
    return template.format(**kwargs)

def send_personalized_message(user_id, template_key, **kwargs):
    msg = render_template(template_key, **kwargs)
    send_notification(user_id, msg)

def broadcast_message(user_ids, message):
    for uid in user_ids:
        send_notification(uid, message)

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(render_template("welcome", name="Luca"))
    send_personalized_message(1, "badge", name="Luca", badge="Director Unlocked")
