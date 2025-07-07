"""
Modulo: automation.py
Gestisce tutte le automazioni di Massimo AI: scheduling, reminder, follow-up, notifiche, drip-campaign, alert, micro-learning.
Motore centrale per rendere il sistema intelligente, proattivo e davvero scalabile.
Pronto per estensioni multicanale (Telegram, WhatsApp, Email, dashboard, social).
"""

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from notifications import send_notification
from data_manager import get_user_data, update_user_data, get_all_users
from gamification import assign_badge
from quiz_module import assign_quiz, check_quiz_results

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def start_scheduler():
    """Avvia lo scheduler delle automazioni (da chiamare in main.py)."""
    scheduler.start()
    logger.info("Automation scheduler avviato.")

def stop_scheduler():
    scheduler.shutdown()
    logger.info("Automation scheduler arrestato.")

# --- AUTOMAZIONI CORE ---

def schedule_onboarding_reminder(user_id, delay_hours=2):
    """Invia un reminder onboarding dopo X ore dal primo accesso."""
    run_time = datetime.now() + timedelta(hours=delay_hours)
    scheduler.add_job(
        func=send_notification,
        trigger='date',
        run_date=run_time,
        args=[user_id, "Non hai completato il percorso di onboarding. Vuoi continuare ora?"],
        id=f"onboarding_reminder_{user_id}",
        replace_existing=True
    )

def schedule_inactivity_alert(user_id, delay_days=3):
    """Avvisa un utente che non è più attivo da X giorni."""
    run_time = datetime.now() + timedelta(days=delay_days)
    scheduler.add_job(
        func=send_notification,
        trigger='date',
        run_date=run_time,
        args=[user_id, "Ti abbiamo sentito poco ultimamente! Vuoi scoprire cosa puoi sbloccare oggi con Massimo AI?"],
        id=f"inactivity_alert_{user_id}",
        replace_existing=True
    )

def schedule_drip_campaign(user_id, campaign_steps):
    """Gestisce una drip campaign (es: formazione step by step) verso l’utente."""
    now = datetime.now()
    for idx, (msg, delay_days) in enumerate(campaign_steps):
        run_time = now + timedelta(days=delay_days)
        scheduler.add_job(
            func=send_notification,
            trigger='date',
            run_date=run_time,
            args=[user_id, msg],
            id=f"drip_{user_id}_{idx}",
            replace_existing=True
        )

def schedule_badge_assignment(user_id, badge, trigger_time=None):
    """Assegna un badge automaticamente a un certo orario (o subito se trigger_time=None)."""
    if trigger_time:
        scheduler.add_job(
            func=assign_badge,
            trigger='date',
            run_date=trigger_time,
            args=[user_id, badge],
            id=f"badge_{badge}_{user_id}",
            replace_existing=True
        )
    else:
        assign_badge(user_id, badge)

def auto_assign_quiz(user_id, quiz_id, delay_hours=1):
    """Assegna un quiz all’utente dopo X ore (es. dopo passaggio step o inattività)."""
    run_time = datetime.now() + timedelta(hours=delay_hours)
    scheduler.add_job(
        func=assign_quiz,
        trigger='date',
        run_date=run_time,
        args=[user_id, quiz_id],
        id=f"quiz_{quiz_id}_{user_id}",
        replace_existing=True
    )

def monitor_user_activity():
    """Routine periodica: controlla utenti inattivi e invia reminder."""
    users = get_all_users()
    for user in users:
        last_active = user.get('last_active')
        if last_active and (datetime.now() - last_active).days > 7:
            schedule_inactivity_alert(user['user_id'], delay_days=0)

def schedule_periodic_tasks():
    """Schedula tutte le automazioni ricorrenti (chiamato in main.py)."""
    # Reminder periodici
    scheduler.add_job(
        func=monitor_user_activity,
        trigger='interval',
        hours=24,
        id="monitor_user_activity",
        replace_existing=True
    )

# --- Esempio di utilizzo ---
if __name__ == "__main__":
    start_scheduler()
    # Esempio: schedule_onboarding_reminder(user_id=12345, delay_hours=2)
    # Esempio: schedule_drip_campaign(12345, [("Benvenuto nello step 1!", 0), ("Ecco lo step 2!", 2)])
    # Ricorda di fermare lo scheduler alla chiusura
    # stop_scheduler()
