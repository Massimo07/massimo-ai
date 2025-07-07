"""
Modulo: auto_update.py
Sistema notifiche update: avvisa admin e team se ci sono nuovi moduli, versioni, funzioni (release notes automatiche).
Può scaricare aggiornamenti da repo, notificare in bot o su dashboard.
"""

import logging

logger = logging.getLogger("massimoai.auto_update")

RELEASE_NOTES = [
    {"version": "1.1.0", "date": "2025-06-24", "notes": "Aggiunto logging avanzato e knowledge base live editabile"},
    {"version": "1.0.0", "date": "2025-06-20", "notes": "Massimo AI primo deploy ufficiale"}
    # Popola ogni volta che aggiorni!
]

CURRENT_VERSION = "1.1.0"

def get_latest_release():
    return RELEASE_NOTES[0] if RELEASE_NOTES else {}

def notify_update(channel="telegram"):
    """Notifica admin/team che c’è un aggiornamento."""
    latest = get_latest_release()
    msg = f"🚀 Massimo AI aggiornato alla versione {latest['version']} ({latest['date']})\n\nCosa c’è di nuovo:\n{latest['notes']}"
    # Qui puoi mandare la notifica reale (bot, email, dashboard)
    logger.info(msg)

# --- ESEMPIO USO ---
if __name__ == "__main__":
    notify_update()
