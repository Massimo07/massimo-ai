"""
Modulo: feedback.py
Gestione feedback utenti: raccolta valutazioni (emoji, punteggi, commenti), NPS automatico, alert admin in caso di problemi.
Pronto per integrare ovunque (post-risposta, post-onboarding, post-azione chiave).
"""

import logging
from data_manager import update_user_data, get_user_data

logger = logging.getLogger("massimoai.feedback")

FEEDBACKS = []

def collect_feedback(user_id, score, comment=""):
    """
    Registra un feedback (1-10, emoji, commento).
    """
    user = get_user_data(user_id)
    entry = {
        "user_id": user_id,
        "name": user.get("name") if user else None,
        "score": score,
        "comment": comment
    }
    FEEDBACKS.append(entry)
    logger.info(f"Feedback ricevuto: {entry}")
    # Aggiorna NPS user in data_manager/bi
    update_user_data(user_id, nps=score)
    # Alert admin se punteggio basso
    if score < 6:
        logger.warning(f"ALERT: Feedback negativo da {user_id}: {comment}")

def get_feedbacks(limit=100):
    return FEEDBACKS[-limit:]

def avg_nps():
    if not FEEDBACKS:
        return 0
    return sum(f["score"] for f in FEEDBACKS) / len(FEEDBACKS)

# --- ESEMPIO USO ---
if __name__ == "__main__":
    collect_feedback(1, 10, "Top servizio!")
    collect_feedback(2, 4, "Troppo lento.")
    print(get_feedbacks())
    print("NPS medio:", avg_nps())
