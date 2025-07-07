"""
Modulo: crm.py
Customer Relationship Management: gestione lead, clienti, prospect, follow-up, scoring, tagging, stato, automazioni.
Perfetto per segmentare, monitorare, convertire e seguire ogni utente/team member di Massimo AI.
"""

import logging
from data_manager import get_all_users, update_user_data

logger = logging.getLogger(__name__)

def add_lead(user_id, info):
    """
    Aggiunge/aggiorna un lead nel CRM.
    """
    update_user_data(user_id, **info)
    logger.info(f"Lead aggiunto o aggiornato: {user_id} — {info}")

def list_leads(status=None):
    """
    Elenca tutti i lead filtrati per status (prospect, iscritto, attivo, inattivo...).
    """
    users = get_all_users()
    return [u for u in users if (not status or u.get("status") == status)]

def followup_lead(user_id, message):
    """
    Registra una nuova attività di follow-up e invia notifica.
    """
    # Qui puoi loggare nel DB le attività di follow-up
    logger.info(f"Follow-up inviato a {user_id}: {message}")

def score_lead(user_id, score):
    """
    Aggiorna il lead scoring dell’utente.
    """
    update_user_data(user_id, lead_score=score)
    logger.info(f"Score aggiornato per {user_id}: {score}")

# --- Esempio di utilizzo ---
if __name__ == "__main__":
    add_lead(12345, {"name": "Luca", "status": "prospect"})
    followup_lead(12345, "Ti ricordo la promo di giugno!")
    score_lead(12345, 8)
    print(list_leads("prospect"))
