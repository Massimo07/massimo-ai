"""
Modulo: alert.py
Invia notifiche real-time (Telegram/email) a admin/superuser in caso di eventi critici, errori, feedback negativo, nuovi iscritti VIP, anomalie.
Pronto per ogni piattaforma. Espandibile a Slack, SMS, WhatsApp, dashboard.
"""

import logging

logger = logging.getLogger("massimoai.alert")

ADMIN_CHAT_ID = 123456789  # Inserisci il tuo chat_id Telegram admin

def send_alert_telegram(bot, message):
    """
    Invia un alert urgente via Telegram a admin.
    """
    try:
        bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"🚨 ALERT Massimo AI 🚨\n{message}")
        logger.info("Alert Telegram inviato.")
    except Exception as e:
        logger.error(f"Errore invio alert Telegram: {e}")

def send_alert_email(email, subject, message):
    """
    Invia un alert urgente via email (integra con libreria SMTP/emailing).
    """
    # Demo: stampa a log — inserisci qui invio reale!
    logger.info(f"Inviato alert email a {email} — Subject: {subject}\n{message}")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    send_alert_telegram(None, "Test alert! (devi passare bot reale)")
    send_alert_email("admin@magicteam.it", "Errore critico", "Il sistema richiede attenzione immediata.")
