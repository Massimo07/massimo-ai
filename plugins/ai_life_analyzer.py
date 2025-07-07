"""
Modulo: ai_life_analyzer.py
Analisi benessere olistico: monitora performance, umore, equilibrio, salute mentale. Suggerisce pause, sport, meditazione, motivazione. Approccio “life-first”.
"""

import random

LIFE_SCORES = {}

def record_wellness(user_id, mood, sleep_hours, activity, notes=""):
    score = (sleep_hours * 10) + (20 if activity else 0) + (10 if mood == "positivo" else -10)
    LIFE_SCORES[user_id] = score
    return f"Wellness score: {score}"

def wellness_advice(user_id):
    score = LIFE_SCORES.get(user_id, 0)
    if score < 40:
        return "Fermati, prenditi una pausa e dedicati a te stesso! Una breve meditazione o una passeggiata aiutano."
    elif score < 80:
        return "Continua così, ma non dimenticare di prenderti cura di corpo e mente."
    else:
        return "Ottimo equilibrio! Sei nella condizione ideale per raggiungere i tuoi sogni."

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(record_wellness(1, "positivo", 7, True))
    print(wellness_advice(1))
