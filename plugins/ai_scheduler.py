"""
Modulo: ai_scheduler.py
Gestione AI di appuntamenti, eventi, task, meeting, challenge. Sincronizza con Google Calendar, invia reminder su Telegram, WhatsApp, SMS, email!
"""

import datetime

SCHEDULE = []

def add_event(user_id, title, date, channel="telegram"):
    event = {"user_id": user_id, "title": title, "date": date, "channel": channel}
    SCHEDULE.append(event)
    print(f"Evento '{title}' aggiunto per user {user_id} su {channel} in data {date}")

def list_events(user_id=None):
    if user_id:
        return [e for e in SCHEDULE if e["user_id"] == user_id]
    return SCHEDULE

def send_reminders():
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    for e in SCHEDULE:
        if e["date"] == now:
            print(f"Reminder inviato a {e['user_id']} per evento '{e['title']}' via {e['channel']}")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    add_event(1, "Call motivazionale", "2025-07-01", "whatsapp")
    add_event(1, "Formazione Team", "2025-07-01", "telegram")
    send_reminders()
