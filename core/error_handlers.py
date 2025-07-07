"""
core/error_handlers.py – Gestione errori centralizzata, logging, alert founder.
"""

import logging
import traceback

def handle_error(e, alert_founder=False):
    logging.error(f"[ERROR] {type(e).__name__}: {e}")
    logging.error(traceback.format_exc())
    if alert_founder:
        # Qui potresti inviare alert via Telegram/email al founder
        logging.warning("[ERROR] Alert founder attivo!")
