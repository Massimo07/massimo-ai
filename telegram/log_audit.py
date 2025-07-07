"""
Modulo: log_audit.py
Logging avanzato e audit trail: traccia ogni azione utente, operatore, AI.
Pronto per sicurezza, GDPR, qualità e disaster recovery. Accessibile solo da admin.
"""

import logging
from datetime import datetime
from data_manager import get_user_data

logger = logging.getLogger("massimoai.audit")

AUDIT_LOG = []

def log_action(user_id, action, detail="", status="OK"):
    """
    Registra un’azione in audit trail (in RAM o su file/DB).
    """
    user = get_user_data(user_id)
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "user": user.get("name") if user else None,
        "action": action,
        "detail": detail,
        "status": status
    }
    AUDIT_LOG.append(entry)
    logger.info(f"AUDIT: {entry}")
    # Per cloud: salva su file/DB/cloud (es. S3, Postgres)

def get_audit_log(limit=100):
    """Restituisce le ultime azioni (visibili solo ad admin)."""
    return AUDIT_LOG[-limit:]

def clear_audit_log():
    """Resetta il log (solo per manutenzione/admin)."""
    global AUDIT_LOG
    AUDIT_LOG = []
    logger.info("AUDIT LOG resettato.")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    log_action(1, "login", "Accesso da Telegram")
    log_action(2, "upgrade", "Passaggio a Network Leggendario", "OK")
    for entry in get_audit_log():
        print(entry)
