"""
Modulo: ai_inbox.py
Inbox smart: centralizza e smista messaggi/team/chat/alert/task per priorità, lingua, argomento. AI routing e risposta automatica.
"""

INBOX = []

def add_message(user_id, text, priority="normale", lang="it", topic="info"):
    msg = {
        "user_id": user_id,
        "text": text,
        "priority": priority,
        "lang": lang,
        "topic": topic
    }
    INBOX.append(msg)
    return len(INBOX)

def get_priority_messages(min_priority="alta"):
    prio = {"bassa": 1, "normale": 2, "alta": 3}
    return [m for m in INBOX if prio.get(m["priority"], 2) >= prio.get(min_priority, 2)]

# --- ESEMPIO USO ---
if __name__ == "__main__":
    add_message(1, "Serve info piano marketing", "alta", "it", "marketing")
    print(get_priority_messages("alta"))
