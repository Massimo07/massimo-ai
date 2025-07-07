"""
Modulo: ai_community_pulse.py
Community pulse: analizza messaggi, emoji, feedback, chat del team, misura entusiasmo e coesione, suggerisce azioni per rafforzare il gruppo.
"""

import random

def measure_pulse(messages):
    # messages = ["Grande energia oggi!", "Mi sento poco coinvolto...", ...]
    positive = sum(1 for m in messages if any(w in m.lower() for w in ["grande", "wow", "energia", "grazie", "top"]))
    negative = sum(1 for m in messages if any(w in m.lower() for w in ["stanco", "non", "poco", "problema", "dubbio"]))
    index = 50 + (positive - negative) * 5
    mood = "fortissimo" if index > 60 else "buono" if index > 45 else "da rafforzare"
    return {"pulse_index": index, "mood": mood, "suggestion": "Organizza un mini-evento online di 30 minuti!" if mood != "fortissimo" else "Premia i membri più attivi oggi!"}

# --- ESEMPIO USO ---
if __name__ == "__main__":
    msgs = ["Grande energia oggi!", "Mi sento poco coinvolto...", "Wow che call!", "Oggi problemi su WhatsApp"]
    print(measure_pulse(msgs))
