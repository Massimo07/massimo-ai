"""
Modulo: event_manager.py
Gestisce eventi live, webinar, RSVP, premi automatici. Invio reminder e notifiche su Telegram, email, dashboard.
"""

import datetime

EVENTS = []
RSVP = []

def create_event(title, date, descr, link, premio=None):
    event = {
        "title": title,
        "date": date,
        "descr": descr,
        "link": link,
        "premio": premio
    }
    EVENTS.append(event)
    return event

def add_rsvp(event_title, user_id):
    RSVP.append({"event": event_title, "user_id": user_id, "timestamp": datetime.datetime.now().isoformat()})
    return "Registrazione evento confermata!"

def list_events():
    return EVENTS

def send_reminder(event_title):
    # Demo: Invia reminder via Telegram/email agli iscritti
    iscritti = [r for r in RSVP if r["event"] == event_title]
    print(f"Reminder inviato a {len(iscritti)} iscritti per evento '{event_title}'.")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    create_event("Webinar Magic Team", "2025-07-05 21:00", "Nuove strategie per crescere!", "https://zoom.us/magicteam", "NFT Badge VIP")
    add_rsvp("Webinar Magic Team", 1)
    send_reminder("Webinar Magic Team")
    print(list_events())
