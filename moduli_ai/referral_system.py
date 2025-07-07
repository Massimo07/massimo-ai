"""
Modulo: referral_system.py
Referral & sponsorship: generazione e gestione link referral, scelta sponsor, tracciamento iscrizioni, leaderboard.
Pronto per dashboard, monitoraggio, funnel automatici, accesso multilingua.
"""

import logging
from data_manager import get_user_data, update_user_data, get_all_users

logger = logging.getLogger(__name__)

def generate_referral_link(user_id):
    """Genera un link referral unico per ogni utente."""
    return f"https://liveonplus.it/signup?ref={user_id}"

def select_sponsor(referral_code):
    """Seleziona lo sponsor a partire dal codice referral."""
    return get_user_data(referral_code)

def list_sponsors(province=None):
    """Restituisce una lista filtrata di sponsor (nome, provincia, breve bio)."""
    users = get_all_users()
    sponsors = [u for u in users if u.get("level") and u.get("level") != "Prospect"]
    if province:
        sponsors = [s for s in sponsors if s.get("city") == province]
    return sponsors

def track_registration(user_id, sponsor_id):
    """Collega la registrazione di un nuovo utente a uno sponsor."""
    update_user_data(user_id, sponsor=sponsor_id)
    logger.info(f"Registrazione tracciata: user {user_id} → sponsor {sponsor_id}")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(generate_referral_link(12345))
    print(list_sponsors("Palermo"))
    track_registration(67890, 12345)
