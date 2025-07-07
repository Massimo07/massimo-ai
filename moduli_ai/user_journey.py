"""
Modulo: user_journey.py
Gestisce la timeline di crescita di ogni utente: badge, tappe, quiz, avanzamenti. Visualizzabile in dashboard e chatbot.
"""

import data_manager
import datetime

def record_event(user_id, event, detail=""):
    user = data_manager.get_user_data(user_id)
    journey = user.get("journey", [])
    journey.append({
        "timestamp": datetime.datetime.now().isoformat(),
        "event": event,
        "detail": detail
    })
    data_manager.update_user_data(user_id, journey=journey)

def get_journey(user_id):
    user = data_manager.get_user_data(user_id)
    return user.get("journey", [])

def print_journey(user_id):
    journey = get_journey(user_id)
    for step in journey:
        print(f"[{step['timestamp']}] {step['event']} - {step['detail']}")

if __name__ == "__main__":
    record_event(1, "Registrazione", "Ha iniziato con Massimo AI.")
    record_event(1, "Primo ordine", "Ha acquistato prodotti skincare.")
    print_journey(1)
