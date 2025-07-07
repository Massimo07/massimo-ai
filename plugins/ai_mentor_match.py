"""
Modulo: ai_mentor_match.py
Trova-mentore AI: abbina ogni membro al mentore perfetto secondo obiettivi/competenze, crea micro-percorsi, monitora risultati e feedback.
"""

MENTORS = [
    {"id": 1, "name": "Sara", "skills": ["leadership", "motivazione"]},
    {"id": 2, "name": "Giorgio", "skills": ["vendita", "training"]}
]

def match_mentor(user_goal):
    for m in MENTORS:
        if user_goal in m["skills"]:
            return f"Mentor consigliato: {m['name']} ({user_goal})"
    return "Nessun mentor disponibile ora — prova con un altro goal."

def feedback_mentor(user_id, mentor_id, rating):
    # Demo: tracking feedback
    return f"Feedback ricevuto da {user_id} per mentor {mentor_id}: voto {rating}/5"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(match_mentor("leadership"))
    print(feedback_mentor(4, 1, 5))
