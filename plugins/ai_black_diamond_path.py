"""
Modulo: ai_black_diamond_path.py
Black Diamond Path: roadmap step-by-step per arrivare a Black Diamond — obiettivi, motivazione, alert, rewarding, progressi live e storie ispirazionali.
"""

PATHS = {}

def start_black_diamond(user_id):
    steps = [
        "1. Fissa obiettivo: 60 PV personali/mese per 3 mesi",
        "2. Attiva 4 Director in team",
        "3. Raggiungi 30.000 PV di gruppo/mese",
        "4. Mantieni i risultati per 90 giorni",
        "5. Partecipa a 2 eventi nazionali",
        "6. Crea una storia ispirazionale con Massimo AI"
    ]
    PATHS[user_id] = {"steps": steps, "progress": 0}
    return f"Black Diamond Path iniziato per {user_id}!"

def next_black_diamond_step(user_id):
    path = PATHS.get(user_id)
    if not path:
        return "Nessun percorso trovato!"
    if path["progress"] < len(path["steps"]):
        step = path["steps"][path["progress"]]
        path["progress"] += 1
        return f"Prossimo step: {step}"
    return "Black Diamond raggiunto! Celebrazione AI in arrivo!"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(start_black_diamond(1))
    print(next_black_diamond_step(1))
