"""
Modulo: quiz_competition.py
Gestione quiz competition live/team: domande, classifica, premi, replay, leaderboard aggiornata in real time.
"""

import random

QUIZ = [
    {"q": "Quando è nata Live On Plus?", "a": ["2018", "2020"], "right": 0},
    {"q": "Cos'è un PV?", "a": ["Punto Vendita", "Punto Volume"], "right": 1}
]

SCORES = {}

def start_quiz(user_id):
    SCORES[user_id] = 0
    for q in QUIZ:
        # Demo: risposta random
        answer = random.randint(0, len(q["a"])-1)
        if answer == q["right"]:
            SCORES[user_id] += 1
    return f"Quiz finito! Punteggio: {SCORES[user_id]}/{len(QUIZ)}"

def leaderboard():
    return sorted(SCORES.items(), key=lambda x: x[1], reverse=True)

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(start_quiz(1))
    print(leaderboard())
