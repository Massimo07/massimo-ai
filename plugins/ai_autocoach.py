"""
Modulo: ai_autocoach.py
Coach AI evolutivo: studia feedback, risultati reali, aggiorna piani/consigli/training. Ogni settimana migliori, più efficaci, su misura!
"""

COACH_LOG = []

def log_success(user_id, action, outcome):
    COACH_LOG.append({"user_id": user_id, "action": action, "outcome": outcome})

def generate_training(user_id):
    successes = [l for l in COACH_LOG if l["user_id"] == user_id and l["outcome"] == "successo"]
    n = len(successes)
    if n < 3:
        return "Inizia con i fondamentali del network marketing."
    elif n < 7:
        return "Passa al livello avanzato: gestione team e leadership."
    else:
        return "Training elite: strategie Black Diamond, automatizzazione, crescita esponenziale!"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    log_success(1, "recruitment", "successo")
    log_success(1, "vendita", "successo")
    print(generate_training(1))
