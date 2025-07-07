"""
Modulo: ai_virtual_event_assistant.py
Assistente AI eventi: pianifica, promuove, ricorda eventi. Risponde live alle domande, invia materiali, gestisce RSVP e premi post-evento.
"""

EVENTS = []

def create_event(title, date, materials, link):
    event = {"title": title, "date": date, "materials": materials, "link": link}
    EVENTS.append(event)
    return event

def send_reminder(event_title):
    for e in EVENTS:
        if e["title"] == event_title:
            print(f"Reminder evento: {e['title']} in data {e['date']} - link: {e['link']}")

def live_qa(question):
    # Demo: risponde sempre positivo, in reale integri OpenAI
    return f"Risposta AI: ottima domanda! Approfondiamo insieme…"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    create_event("Super Webinar", "2025-07-10", ["slide.pdf"], "https://zoom.us/...")
    send_reminder("Super Webinar")
    print(live_qa("Come si diventa Black Diamond?"))
