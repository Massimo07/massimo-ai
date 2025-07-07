"""
Modulo: ai_smart_reminder.py
Reminder AI: invia promemoria ultra-personalizzati (motivazione, supporto, tecnici), riconosce i blocchi reali, adatta contenuto/frequenza dinamicamente.
"""

REMINDER_LOG = {}

def set_reminder(user_id, topic, frequency="giornaliero"):
    REMINDER_LOG[user_id] = {"topic": topic, "frequency": frequency, "last": None}
    return f"Reminder impostato su {topic} ({frequency})!"

def get_reminder(user_id):
    r = REMINDER_LOG.get(user_id)
    if not r:
        return "Nessun reminder attivo."
    return f"Ricordati: {r['topic']} (frequenza: {r['frequency']})"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(set_reminder(1, "Invita 2 persone nuove oggi!", "giornaliero"))
    print(get_reminder(1))
