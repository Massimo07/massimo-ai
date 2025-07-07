"""
Modulo: quiz_module.py
Gestione quiz e micro-learning per Massimo AI: domande, correzioni, scoring, badge.
Supporta quiz onboarding, formazione, quiz motivazionali, validazione livello, ripetizione automatica.
"""

import logging
from notifications import send_notification
from data_manager import update_user_data, get_user_data

logger = logging.getLogger(__name__)

QUIZZES = {
    "onboarding": [
        {"question": "Cos’è Live On Plus?", "answer": "Un’azienda di network marketing italiana"},
        {"question": "Quanti livelli ha il piano compensi base?", "answer": "5"},
        {"question": "Chi può accedere ai badge?", "answer": "Tutti gli iscritti"},
    ]
    # Aggiungi quiz per ogni percorso!
}

def assign_quiz(user_id, quiz_name):
    """
    Assegna un quiz all’utente e invia la prima domanda.
    """
    quiz = QUIZZES.get(quiz_name)
    if not quiz:
        logger.warning(f"Quiz {quiz_name} non trovato.")
        return
    update_user_data(user_id, current_quiz=quiz_name, quiz_step=0)
    send_notification(user_id, f"Quiz '{quiz_name}' iniziato!\n{quiz[0]['question']}")

def check_quiz_results(user_id, answers):
    """
    Corregge le risposte e assegna badge se superato.
    """
    user = get_user_data(user_id)
    quiz_name = user.get("current_quiz")
    quiz = QUIZZES.get(quiz_name)
    if not quiz:
        return False
    score = sum(1 for i, q in enumerate(quiz) if answers[i].strip().lower() == q["answer"].strip().lower())
    result = score == len(quiz)
    if result:
        send_notification(user_id, "Complimenti, hai superato il quiz!")
        # Puoi assegnare badge qui!
    else:
        send_notification(user_id, "Non tutte le risposte sono corrette. Puoi riprovare!")
    return result

# --- ESEMPIO USO ---
if __name__ == "__main__":
    assign_quiz(1, "onboarding")
    check_quiz_results(1, ["Un’azienda di network marketing italiana", "5", "Tutti gli iscritti"])
