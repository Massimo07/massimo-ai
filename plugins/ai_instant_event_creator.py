"""
Modulo: ai_instant_event_creator.py
Crea/promuove eventi, contest, flash challenge in un click, invia inviti smart, gestisce RSVP e reward, genera replay/video highlights automatici.
"""

EVENTS = []

def create_instant_event(title, date, reward, replay=True):
    EVENTS.append({"title": title, "date": date, "reward": reward, "replay": replay})
    return f"Evento '{title}' creato per il {date} — Premio: {reward}"

def invite_team(event_title):
    for e in EVENTS:
        if e["title"] == event_title:
            print(f"Invito smart inviato per l’evento: {e['title']}!")

def auto_replay(event_title):
    # Demo: genera link replay
    for e in EVENTS:
        if e["title"] == event_title and e["replay"]:
            retu
