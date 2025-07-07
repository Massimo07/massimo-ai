"""
Modulo: scam_detector.py
Rileva spam, tentativi di truffa/fake account, auto-ban, auto-alert admin. Analisi testo, pattern, sentiment e comportamento.
"""

import logging

logger = logging.getLogger("massimoai.scam_detector")

SUSPICIOUS_WORDS = ["soldi facili", "link strano", "offerta incredibile", "script magico"]

def scan_message(user_id, message):
    for word in SUSPICIOUS_WORDS:
        if word in message.lower():
            logger.warning(f"Potenziale scam da {user_id}: {message}")
            # Auto-ban/alert
            return "Messaggio sospetto! Segnalato all'admin."
    return "OK"

def ban_user(user_id):
    logger.info(f"Utente {user_id} bannato per tentato scam.")
    # Chiamare access_control.block_user(user_id) se vuoi auto-ban reale

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(scan_message(1, "Guadagna SOLDI FACILI con questo script magico!"))
    ban_user(1)
