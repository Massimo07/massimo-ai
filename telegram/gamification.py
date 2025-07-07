"""
Modulo: gamification.py
Gestione della gamification di Massimo AI: badge, punti, classifiche, sfide, premi, notifiche motivazionali.
Motore centrale per aumentare engagement e progressi, tutto tracciato e integrabile con dashboard, automation, BI.
"""

import logging
from data_manager import get_user_data, update_user_data, get_all_users
from notifications import send_notification

logger = logging.getLogger(__name__)

BADGES = {
    "Onboarding Master": "Completa tutto l’onboarding",
    "First Sale": "Effettua la tua prima vendita",
    "Director Unlocked": "Diventa Director",
    "Black Diamond": "Raggiungi il massimo livello",
    "Quiz Hero": "Supera 10 quiz"
}

def assign_badge(user_id, badge_name):
    """Assegna un badge all’utente (e notifica)."""
    user = get_user_data(user_id)
    if not user:
        logger.warning(f"assign_badge: utente {user_id} non trovato.")
        return
    badges = set(user.get("badges", []))
    if badge_name in badges:
        return  # già assegnato
    badges.add(badge_name)
    update_user_data(user_id, badges=list(badges))
    send_notification(user_id, f"🏅 Hai ottenuto il badge: {badge_name}!\n{BADGES.get(badge_name, '')}")
    logger.info(f"Badge {badge_name} assegnato a user {user_id}")

def update_leaderboard():
    """Aggiorna la classifica in base a PV Team, badge, quiz, engagement."""
    users = get_all_users()
    leaderboard = sorted(
        users,
        key=lambda u: (u.get("pv_team", 0), len(u.get("badges", [])), u.get("engagement", 0)),
        reverse=True
    )
    # Qui si può salvare su file, database, oppure pubblicare su dashboard/telegram
    logger.info("Leaderboard aggiornata.")
    return leaderboard

def run_challenge(user_id, challenge_name):
    """Gestisce una challenge (sfida) con premi/badge."""
    # Esempio challenge: "Invita 3 amici in una settimana"
    # Logica della challenge qui...
    logger.info(f"Challenge {challenge_name} aggiornata per {user_id}.")

def celebrate_progress(user_id, step):
    """Messaggio motivazionale quando si avanza di step/livello."""
    messages = {
        1: "Bravo! Hai completato il primo step. Avanti così!",
        5: "Sei nella Top 5 del Magic Team! Ora puoi ispirare gli altri.",
        10: "Hai raggiunto il livello Black Diamond! Sei un esempio per tutti!"
    }
    msg = messages.get(step, f"Complimenti, hai completato lo step {step}!")
    send_notification(user_id, msg)
    logger.info(f"Messaggio motivazionale inviato a {user_id} per step {step}")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    assign_badge(1, "Onboarding Master")
    print(update_leaderboard())
    run_challenge(1, "Invita 3 amici")
    celebrate_progress(1, 5)
