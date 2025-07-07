"""
Modulo: ai_soul_coach.py
Soul Coach AI: guida ogni persona a scoprire scopo, talento, missione di vita — supera blocchi interiori, costruisce autostima e ispirazione ogni giorno.
"""

def soul_questionnaire(user_id):
    # Domande profondissime, AI elabora insight personalizzato
    domande = [
        "Qual è il sogno che ti fa alzare dal letto anche nei giorni difficili?",
        "Cosa vorresti lasciare come eredità vera al mondo?",
        "Qual è la paura che vuoi trasformare in forza?",
        "Scrivi una cosa che non hai mai detto a nessuno…"
    ]
    return domande

def soul_answer(user_id, answers):
    return f"Grazie per la tua sincerità. Oggi il tuo potere nascosto è: '{answers[0]}'. Trasformalo in azione con il supporto del Magic Team!"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    domande = soul_questionnaire(1)
    print(domande)
    print(soul_answer(1, ["Voglio essere libero e lasciare un segno"]))
