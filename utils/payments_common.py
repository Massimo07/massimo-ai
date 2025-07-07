"""
/utils/payments_common.py

Utility avanzate per la gestione pagamenti in Massimo AI:
- Logging transazioni
- Validazione dati
- Ricevute e report
- Prevenzione frodi
- Funzioni comuni Stripe/PayPal (estendibile)
"""

import logging
from datetime import datetime

# Configura il logger globale (scrive su file e console)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/payments.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def log_payment_event(event_type: str, user_id: str = None, data=None):
    """
    Logga ogni evento importante del ciclo di pagamento.
    """
    msg = f"[{event_type}]"
    if user_id:
        msg += f" user_id={user_id}"
    if data:
        msg += f" data={data}"
    logging.info(msg)

def validate_payment_data(payment_data: dict, required_fields: list):
    """
    Valida che i dati pagamento includano tutti i campi obbligatori.
    """
    for field in required_fields:
        if field not in payment_data or not payment_data[field]:
            raise ValueError(f"Missing required payment field: {field}")

def generate_receipt(payment_id: str, amount: float, method: str, user_email: str) -> str:
    """
    Genera ricevuta digitale del pagamento (pronta per invio via email).
    """
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return (
        f"Ricevuta Massimo AI\n"
        f"----------------------\n"
        f"Data: {now} UTC\n"
        f"Pagamento: {payment_id}\n"
        f"Importo: {amount:.2f} EUR\n"
        f"Metodo: {method}\n"
        f"Utente: {user_email}\n"
        f"Grazie per aver scelto Massimo AI!"
    )

def is_fraudulent_payment(payment_data: dict) -> bool:
    """
    Esempio di controllo antifrode base (estendibile con AI/analytics):
    """
    # Esempio: blocca se importo troppo alto o paese sospetto
    amount = float(payment_data.get("amount", 0))
    country = payment_data.get("country", "")
    if amount > 9999 or country in ["RU", "KP", "IR"]:
        logging.warning(f"Possibile pagamento fraudolento: {payment_data}")
        return True
    return False

# Estendibile con altre utility: notifiche, backup, reconciliations...
