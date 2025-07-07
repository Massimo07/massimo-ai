"""
Modulo: talent_finder.py
Analizza profili pubblici (LinkedIn, Meta) via scraping/API e AI scoring: trova prospect e li ordina per compatibilità!
"""

import random

def find_prospect(profiles):
    # profiles = [{"name": "Mario", "skills": ["network", "vendita"], "citta": "Palermo"}, ...]
    scored = []
    for p in profiles:
        p["score"] = random.randint(60, 100)  # Demo: AI scoring vero su skill/affinità
        scored.append(p)
    return sorted(scored, key=lambda x: x["score"], reverse=True)

# --- ESEMPIO USO ---
if __name__ == "__main__":
    prospects = [
        {"name": "Mario", "skills": ["network", "vendita"], "citta": "Palermo"},
        {"name": "Luca", "skills": ["ai", "grafica"], "citta": "Roma"}
    ]
    print(find_prospect(prospects))
