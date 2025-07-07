"""
Modulo: ai_time_optimizer.py
Ottimizzazione agenda AI: suggerisce orari/blocchi ottimali, segnala perdite di tempo, propone routine ideali per obiettivi, focus, produttività.
"""

import random

def optimize_time(user_id, tasks, distractions=0):
    total = len(tasks)
    focus = max(1, 8 - distractions)
    if total > 5:
        return "Semplifica: concentra le azioni su massimo 3 task chiave oggi."
    if focus < 5:
        return "Evita interruzioni! Blocca notifiche e dedica 20 minuti ininterrotti al tuo obiettivo più importante."
    return "Sei ben organizzato: programma adesso una pausa di gratitudine e celebra un piccolo risultato!"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(optimize_time(1, ["post social", "follow-up", "chiamata", "ordine"], 2))
