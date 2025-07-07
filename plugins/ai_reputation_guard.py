"""
Modulo: ai_reputation_guard.py
Reputation Guard AI: monitora brand/team su social/web, avvisa su recensioni negative, suggerisce risposte e azioni reputazionali.
"""

NEGATIVES = [
    {"text": "Non mi è arrivato il prodotto!", "author": "Mario", "platform": "Facebook"},
    {"text": "Non ho capito il piano marketing", "author": "Luca", "platform": "Instagram"}
]

def check_reputation():
    # In reale: scraping/social API/monitoring, qui demo
    alerts = []
    for n in NEGATIVES:
        if "non" in n["text"]:
            resp = f"Rispondi pubblicamente: 'Ciao {n['author']}, risolviamo subito! Scrivimi in privato.'"
            alerts.append({"platform": n["platform"], "msg": n["text"], "azione": resp})
    return alerts

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(check_reputation())
