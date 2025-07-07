"""
Modulo: drip_automation.py
Gestione delle drip-campaign automatiche di Massimo AI.
Permette di inviare contenuti formativi, reminder, materiali motivazionali e sequenze onboarding a intervalli personalizzati, su più canali (Telegram, WhatsApp, Email).
Sistema pronto per multicanalità, personalizzazione step, logging, analytics e auto-escalation.
"""

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from notifications import send_notification
from data_manager import get_user_data, update_user_data
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler()

# Definizione di una drip campaign (puoi avere più campagne)
DRIP_CAMPAIGNS = {
    "onboarding_base": [
        {"step": 1, "delay_hours": 0, "message": "Benvenuto/a nel Magic Team! Inizia qui il tuo percorso: https://liveonplus.it/onboarding"},
        {"step": 2, "delay_hours": 24, "message": "Hai già esplorato la dashboard? Ecco i vantaggi del primo ordine: ..."},
        {"step": 3, "delay_hours": 48, "message": "Scopri come guadagnare di più: leggi il piano marketing Live On Plus."},
        {"step": 4, "delay_hours": 72, "message": "Hai domande? Scrivi a Massimo AI: sono qui per te, ogni giorno!"},
    ],
    # Puoi definire altre sequenze: formazione avanzata, motivazione, retention, recupero inattivi, promo...
}

def start_drip_campaign(user_id, campaign_name):
    """
    Inizia una drip-campaign su un utente (drip sequenziale, personalizzata).
    """
    user = get_user_data(user_id)
    if not user:
        logger.warning(f"start_drip_campaign: utente {user_id} non trovato.")
        return
    campaign = DRIP_CAMPAIGNS.get(campaign_name)
    if not campaign:
        logger.warning(f"start_drip_campaign: campagna {campaign_name} non trovata.")
        return
    now = datetime.now()
    for step in campaign:
        run_time = now + timedelta(hours=step["delay_hours"])
        scheduler.add_job(
            func=send_notification,
            trigger="date",
            run_date=run_time,
            args=[user_id, step["message"]],
            id=f"drip_{campaign_name}_{user_id}_{step['step']}",
            replace_existing=True
        )
        logger.info(f"Drip automation schedulata per {user_id} step {step['step']} alle {run_time}")

def cancel_drip_campaign(user_id, campaign_name):
    """
    Cancella tutti i job drip di una campagna su un utente.
    """
    campaign = DRIP_CAMPAIGNS.get(campaign_name)
    if not campaign:
        return
    for step in campaign:
        job_id = f"drip_{campaign_name}_{user_id}_{step['step']}"
        try:
            scheduler.remove_job(job_id)
            logger.info(f"Drip automation cancellata: {job_id}")
        except Exception:
            pass

def is_drip_active(user_id, campaign_name):
    """
    Verifica se una drip-campaign è attiva per un utente.
    """
    campaign = DRIP_CAMPAIGNS.get(campaign_name)
    if not campaign:
        return False
    for step in campaign:
        job_id = f"drip_{campaign_name}_{user_id}_{step['step']}"
        if scheduler.get_job(job_id):
            return True
    return False

def start_scheduler():
    scheduler.start()
    logger.info("Drip automation scheduler avviato.")

# --- Esempio di utilizzo diretto ---
if __name__ == "__main__":
    start_scheduler()
    # start_drip_campaign(1, "onboarding_base")
    # cancel_drip_campaign(1, "onboarding_base")
    # print(is_drip_active(1, "onboarding_base"))
