"""
Modulo: ai_magic_mentor_universe.py
Mentor Universe AI: mappa mentor, ranking, abbina mentee/mentor, archivia sessioni, assegna badge, crea stories e video di successo per ogni relazione.
"""

MENTOR_MAP = {}

def add_mentor(mentor_id, name, area):
    MENTOR_MAP[mentor_id] = {"name": name, "area": area, "mentees": []}
    return f"Mentor {name} registrato su area '{area}'."

def assign_mentee(mentor_id, mentee_id):
    MENTOR_MAP[mentor_id]["mentees"].append(mentee_id)
    return f"Mentee {mentee_id} assegnato a mentor {mentor_id}!"

def mentor_story(mentor_id):
    m = MENTOR_MAP.get(mentor_id)
    if not m:
        return "Mentor non trovato."
    return f"Mentor {m['name']} ({m['area']}): {len(m['mentees'])} mentee attivi."

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(add_mentor(11, "Luca", "mindset"))
    print(assign_mentee(11, 4))
    print(mentor_story(11))
