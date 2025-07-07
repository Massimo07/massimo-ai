"""
Modulo: sponsor_map.py
Gestione sponsor nel team Massimo AI: elenco, scelta, filtro per provincia/skills, ranking, assegnazione referral link.
Pronto per onboarding, dashboard e funnel trasparente.
"""

import logging
from data_manager import get_all_users

logger = logging.getLogger(__name__)

def list_all_sponsors():
    """Restituisce lista sponsor (nome, provincia, descrizione, referral link)."""
    users = get_all_users()
    return [
        {
            "name": u["name"],
            "province": u.get("city"),
            "bio": u.get("bio", ""),
            "referral_link": f"https://liveonplus.it/signup?ref={u['user_id']}"
        }
        for u in users if u.get("level") and u["level"] != "Prospect"
    ]

def filter_sponsors(province=None):
    """Filtra sponsor per provincia."""
    return [s for s in list_all_sponsors() if not province or s["province"] == province]

def sponsor_ranking():
    """Ranking sponsor per risultati."""
    sponsors = list_all_sponsors()
    # Demo: ranking per PV Team (o altre metriche)
    sponsors.sort(key=lambda s: s.get("pv_team", 0), reverse=True)
    return sponsors

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(filter_sponsors("Palermo"))
    print(sponsor_ranking())
