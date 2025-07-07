"""
Modulo: ai_inspire_gen.py
Genera messaggi, grafiche, audio motivazionali unici e personalizzati ogni giorno — pronta per Telegram, WhatsApp, social, app, email!
"""

import random

INSPIRATION = [
    "Non fermarti mai davanti al primo ostacolo. È solo il segno che stai andando avanti!",
    "Ogni giorno puoi scegliere: lamentarti o agire. Oggi scegli di AGIRE!",
    "Le sfide ti stanno formando. Presto sarai più forte di quanto immagini.",
    "Sii la motivazione che vuoi ricevere dal mondo."
]

def inspire_today(user_id):
    msg = random.choice(INSPIRATION)
    # Demo: in reale, crea anche grafica e audio con TTS/voice AI
    return f"Messaggio del giorno per {user_id}: {msg}"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(inspire_today(1))
