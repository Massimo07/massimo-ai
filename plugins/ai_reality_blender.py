"""
Modulo: ai_reality_blender.py
Crea esperienze miste reale/digitale: quiz e sfide fisiche + digitali, badge QR, caccia al tesoro, reward istantanei anche fisici e NFT!
"""

import random

MISSIONS = [
    {"desc": "Fai una foto mentre presenti Live On Plus a una persona nuova!"},
    {"desc": "Scansiona il QR al prossimo evento live."},
    {"desc": "Pubblica una storia Instagram con #MagicTeam e mostra la notifica."}
]

def next_mission():
    mission = random.choice(MISSIONS)
    return f"Missione della settimana: {mission['desc']}"

def reward_mission(user_id, mission):
    # Demo: premio fisico/NFT
    return f"Premio per {user_id} — Badge NFT sbloccato grazie alla mission: {mission}"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    m = next_mission()
    print(m)
    print(reward_mission(1, m))

