"""
Modulo: advisor.py
AI advisor intelligente: suggerisce e abbina sponsor migliore per ogni nuovo iscritto, in base a skills, zona, obiettivi, attività, affinità.
"""

import data_manager
import random

def best_sponsor_match(new_user):
    # Demo: seleziona sponsor più attivo nella provincia
    sponsors = [u for u in data_manager.get_all_users() if u.get("level") and u.get("city") == new_user.get("city")]
    if sponsors:
        return random.choice(sponsors)
    # Fallback: sponsor con punteggio più alto
    sponsors = sorted([u for u in data_manager.get_all_users() if u.get("level")], key=lambda x: x.get("score", 0), reverse=True)
    return sponsors[0] if sponsors else None

# --- ESEMPIO USO ---
if __name__ == "__main__":
    new_user = {"city": "Palermo"}
    print(best_sponsor_match(new_user))
