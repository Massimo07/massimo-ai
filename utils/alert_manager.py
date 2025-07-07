import logging
import requests

def send_alert(message: str, level: str = "info"):
    # Puoi collegare Slack, Telegram, Discord, email, PagerDuty, ecc.
    logging.log(getattr(logging, level.upper(), logging.INFO), message)
    # Esempio Telegram:
    # requests.post("https://api.telegram.org/bot.../sendMessage", ...)
