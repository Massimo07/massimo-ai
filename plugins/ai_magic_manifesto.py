"""
Modulo: ai_magic_manifesto.py
Manifesto team AI: crea/aggiorna Manifesto, mission, valori e regole, motiva ogni mese la community con una dichiarazione d’intenti “live”.
"""

import datetime

MANIFESTO = {"valori": [], "mission": "", "last_update": ""}

def set_manifesto(valori, mission):
    MANIFESTO["valori"] = valori
    MANIFESTO["mission"] = mission
    MANIFESTO["last_update"] = datetime.date.today().isoformat()
    return "Manifesto aggiornato!"

def show_manifesto():
    return f"MISSION: {MANIFESTO['mission']}\nVALORI: {', '.join(MANIFESTO['valori'])}\nUltimo update: {MANIFESTO['last_update']}"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    set_manifesto(["crescita", "aiuto reciproco", "onestà"], "Diventare la community più ispirante d’Europa")
    print(show_manifesto())
