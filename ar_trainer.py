"""
Modulo: ar_trainer.py
Modulo base AR: prepara dati/quiz per training in realtà aumentata (esportabili in piattaforme ARKit/ARCore, Zappar ecc.).
"""

import json

def export_ar_quiz(quiz_title, questions):
    # questions = [{"q": "Domanda?", "a": ["ris1", "ris2"], "right": 0}, ...]
    data = {
        "quiz_title": quiz_title,
        "questions": questions,
        "export_time": "2025-06-24T10:01"
    }
    fname = f"ar_quiz_{quiz_title.replace(' ','_')}.json"
    with open(fname, "w") as f:
        json.dump(data, f, indent=2)
    return fname

# --- ESEMPIO USO ---
if __name__ == "__main__":
    quiz = [
        {"q": "Cos'è il Network Marketing?", "a": ["Vendita diretta", "Borsa valori"], "right": 0},
        {"q": "Qual è il tuo obiettivo?", "a": ["Libertà", "Noia"], "right": 0}
    ]
    print(export_ar_quiz("Onboarding Magic Team", quiz))
