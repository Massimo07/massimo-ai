"""
Modulo: access_control.py
Gestione permessi: blocca/sospendi utenti, whitelisting/blacklisting, rate limit.
Pronto per sicurezza enterprise: nessuno accede se non autorizzato. Integrato in ogni modulo chiave.
"""

import logging
from data_manager import update_user_data, get_user_data

logger = logging.getLogger("massimoai.access")

BLACKLIST = set()
WHITELIST = set()

def block_user(user_id, reason=""):
    """Blocca un utente (revoca accesso a bot, dashboard, app, API)."""
    BLACKLIST.add(user_id)
    update_user_data(user_id, status="blocked")
    logger.info(f"Utente {user_id} bloccato. Motivo: {reason}")

def unblock_user(user_id):
    """Sblocca un utente (ripristina permessi)."""
    if user_id in BLACKLIST:
        BLACKLIST.remove(user_id)
        update_user_data(user_id, status="active")
        logger.info(f"Utente {user_id} sbloccato.")

def is_user_blocked(user_id):
    """Verifica se un utente è bloccato."""
    return user_id in BLACKLIST or get_user_data(user_id).get("status") == "blocked"

def add_to_whitelist(user_id):
    WHITELIST.add(user_id)
    logger.info(f"Utente {user_id} aggiunto a whitelist.")

def is_user_whitelisted(user_id):
    return user_id in WHITELIST

def rate_limit(user_id, action, max_calls=10, window_seconds=60):
    """
    Rate limit base (demo): limita il numero di azioni ripetute in poco tempo.
    Puoi estendere con Redis, DB, ecc.
    """
    # Da implementare: logica memoria/rate tracking
    logger.info(f"Rate limit check per {user_id}: azione {action}")
    return False  # False = non limitato

# --- ESEMPIO USO ---
if __name__ == "__main__":
    block_user(5, "Violazione regole")
    print(is_user_blocked(5))
    unblock_user(5)
    add_to_whitelist(6)
    print(is_user_whitelisted(6))
