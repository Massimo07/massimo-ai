"""
Modulo: ai_network_sentinel.py
Sentinella AI: monitora performance, segnala cali di attività, allerta crisi, suggerisce azioni correttive per evitare abbandoni o cali PV.
"""

import random

NETWORK = [{"user_id": 1, "pv": 60, "trend": "stabile"}, {"user_id": 2, "pv": 30, "trend": "in calo"}]

def analyze_network():
    alerts = []
    for u in NETWORK:
        if u["trend"] == "in calo" or u["pv"] < 40:
            alerts.append(f"Allerta: utente {u['user_id']} in calo! Azione consigliata: follow-up personale, premi motivazionali.")
    return alerts

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(analyze_network())
