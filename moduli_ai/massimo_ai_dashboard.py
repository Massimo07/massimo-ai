import json
import os

def carica_utenti():
    path = "massimo_ai/users"
    utenti = []
    if os.path.exists(path):
        for file in os.listdir(path):
            if file.endswith(".json"):
                with open(os.path.join(path, file), "r", encoding="utf-8") as f:
                    utenti.append(json.load(f))
    return utenti

def stats_dashboard():
    utenti = carica_utenti()
    per_livello = {}
    for u in utenti:
        lvl = u.get("livello", "info_free")
        per_livello.setdefault(lvl, []).append(u)
    print("Statistiche utenti per livello:")
    for lvl, arr in per_livello.items():
        print(f" - {lvl}: {len(arr)} iscritti")
    print("Totale utenti:", len(utenti))

def main():
    stats_dashboard()
    # Espandi con tutte le funzioni admin che vuoi

if __name__ == "__main__":
    main()
