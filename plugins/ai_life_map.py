"""
Modulo: ai_life_map.py
Life Map AI: crea mappa grafica eventi chiave/successi/obiettivi; consiglia nuove “direzioni”, suggerisce svolte, celebra traguardi e nuove relazioni.
"""

LIFE_MAPS = {}

def add_life_event(user_id, event, category):
    LIFE_MAPS.setdefault(user_id, []).append({"event": event, "category": category})

def show_life_map(user_id):
    events = LIFE_MAPS.get(user_id, [])
    return [f"{e['event']} ({e['category']})" for e in events]

# --- ESEMPIO USO ---
if __name__ == "__main__":
    add_life_event(1, "Inizio percorso Magic Team", "inizio
