"""
Modulo: predictive.py
Modulo di analytics predittiva: identifica utenti a rischio abbandono, stima crescita, suggerisce azioni per prevenire churn, forecast avanzamenti.
Integrabile con BI, CRM, automation, alert.
"""

import logging
from data_manager import get_all_users
from datetime import datetime

logger = logging.getLogger(__name__)

def predict_churn(user):
    """
    Ritorna True se l’utente è a rischio abbandono.
    (Demo: usa regole semplici, sostituisci con modello ML se vuoi)
    """
    last_active = user.get("last_active")
    engagement = user.get("engagement", 0)
    pv = user.get("pv_mese", 0)
    if not last_active:
        return True
    days = (datetime.now() - last_active).days
    if days > 15 or engagement < 3 or pv < 10:
        return True
    return False

def user_progress_forecast(user):
    """
    Suggerisce azioni per accelerare la crescita (demo).
    """
    if user.get("pv_mese", 0) < 60:
        return "Prova a coinvolgere un nuovo cliente questa settimana!"
    elif user.get("level") == "Director":
        return "Per diventare Black Diamond, guida almeno 4 Director!"
    else:
        return ""

def churn_report():
    """
    Restituisce elenco utenti a rischio abbandono.
    """
    users = get_all_users()
    return [u for u in users if predict_churn(u)]

# --- ESEMPIO USO ---
if __name__ == "__main__":
    for u in churn_report():
        print(f"Rischio abbandono: {u['name']}")
