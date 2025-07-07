"""
Modulo: ai_genius_injection.py
Ogni settimana AI invia idee geniali, shock phrase, micro-innovazioni: chi le mette in pratica per primo… viene premiato e sale di ranking!
"""

import random

GENIUS_IDEAS = [
    "Prova a lanciare una call di brainstorming lampo ogni venerdì mattina.",
    "Crea una rubrica 'Storie vere del Magic Team' sui tuoi social.",
    "Invita il team a una challenge silenziosa: fare un’azione buona senza dirlo.",
    "Trasforma ogni feedback negativo in un post di crescita."
]

def inject_genius():
    idea = random.choice(GENIUS_IDEAS)
    return f"IDEA GENIALE DELLA SETTIMANA: {idea}"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(inject_genius())
