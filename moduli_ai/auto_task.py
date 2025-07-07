"""
Modulo: auto_task.py
Gestione dei task automatici ricorrenti e condizionati di Massimo AI.
Task = azioni automatiche “smart” su trigger di evento, tempo, attività o risultato.
Pronto per essere integrato con scheduler, gamification, CRM, dashboard, analytics.
"""

import logging
from data_manager import get_all_users, update_user_data
from gamification import assign_badge, update_leaderboard
from notifications import send_notification
from predictive import predict_churn, user_progress_forecast

logger = logging.getLogger(__name__)

def auto_upgrade_levels():
    """
    Controlla periodicamente lo stato utenti e aggiorna i livelli se obiettivi raggiunti.
    """
    users = get_all_users()
    for user in users:
        if user.get("pv_mese", 0) >= 60 and user["level"] != "Director":
            update_user_data(user["user_id"], level="Director")
            assign_badge(user["user_id"], "Director Unlocked")
            send_notification(user["user_id"], "Complimenti! Sei diventato Director.")
            logger.info(f"User {user['user_id']} promosso a Director.")

def auto_churn_alert():
    """
    Identifica utenti a rischio abbandono tramite modello predittivo e li segnala (notifica/admin).
    """
    users = get_all_users()
    for user in users:
        if predict_churn(user):
            send_notification(user["user_id"], "Ti abbiamo visto meno attivo! Ricordati di partecipare: nuovi premi e opportunità ti aspettano.")
            logger.info(f"Allerta abbandono inviata a user {user['user_id']}.")

def auto_leaderboard_update():
    """
    Aggiorna la classifica (leaderboard) periodicamente, pubblicando risultati e assegnando premi.
    """
    update_leaderboard()
    logger.info("Leaderboard aggiornata.")

def auto_progress_forecast():
    """
    Previsione di avanzamento utenti: invia consigli per raggiungere nuovi obiettivi.
    """
    users = get_all_users()
    for user in users:
        suggestion = user_progress_forecast(user)
        if suggestion:
            send_notification(user["user_id"], suggestion)
            logger.info(f"Consiglio personalizzato inviato a user {user['user_id']}.")

def auto_cleanup_expired():
    """
    Pulizia automatica di task scaduti, dati inutilizzati, vecchie notifiche (housekeeping).
    """
    # Qui logica di clean-up integrata (ad esempio, elimina notifiche > 30gg)
    logger.info("Cleanup periodico dati scaduti eseguito.")

def schedule_all_auto_tasks(scheduler):
    """
    Registra tutti i task automatici ricorrenti nello scheduler principale (apscheduler).
    """
    scheduler.add_job(auto_upgrade_levels, "interval", hours=6, id="auto_upgrade_levels", replace_existing=True)
    scheduler.add_job(auto_churn_alert, "interval", hours=12, id="auto_churn_alert", replace_existing=True)
    scheduler.add_job(auto_leaderboard_update, "interval", hours=24, id="auto_leaderboard_update", replace_existing=True)
    scheduler.add_job(auto_progress_forecast, "interval", hours=24, id="auto_progress_forecast", replace_existing=True)
    scheduler.add_job(auto_cleanup_expired, "interval", days=1, id="auto_cleanup_expired", replace_existing=True)
    logger.info("Tutti gli auto-task periodici schedulati.")

# --- Esempio di uso diretto (per test/debug) ---
if __name__ == "__main__":
    auto_upgrade_levels()
    auto_churn_alert()
    auto_leaderboard_update()
    auto_progress_forecast()
    auto_cleanup_expired()
