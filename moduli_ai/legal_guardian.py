"""
Modulo: legal_guardian.py
Monitor automatico GDPR/privacy: log accessi, consenso cookie, verifica compliance, alert data breach.
"""

import logging

logger = logging.getLogger("massimoai.legal_guardian")

CONSENTS = []

def log_consent(user_id, type_consent, timestamp):
    CONSENTS.append({
        "user_id": user_id,
        "type": type_consent,
        "timestamp": timestamp
    })
    logger.info(f"Consenso {type_consent} loggato per {user_id}.")

def check_compliance():
    # Demo: verifica se tutti hanno dato consenso base
    missing = [c for c in CONSENTS if c["type"] != "base"]
    if missing:
        logger.warning("Utenti senza consenso base!")
        return False
    return True

def alert_data_breach(details):
    logger.error(f"Data breach: {details}")
    # Qui puoi inviare alert/email agli admin

# --- ESEMPIO USO ---
if __name__ == "__main__":
    log_consent(1, "base", "2025-06-24T09:15")
    print(check_compliance())
    alert_data_breach("Test data breach simulato!")
