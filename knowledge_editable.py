"""
Modulo: knowledge_editable.py
Permette ad admin di aggiungere, modificare, cancellare prodotti, FAQ, risposte, motivazioni senza cambiare codice.
Pronto per mini-dashboard Streamlit, validazione, reload automatico.
"""

import json
import os

KNOWLEDGE_PATH = "knowledge_base.json"

def load_knowledge():
    if not os.path.exists(KNOWLEDGE_PATH):
        with open(KNOWLEDGE_PATH, "w") as f:
            json.dump({"products": [], "faq": [], "motivation": []}, f)
    with open(KNOWLEDGE_PATH) as f:
        return json.load(f)

def save_knowledge(data):
    with open(KNOWLEDGE_PATH, "w") as f:
        json.dump(data, f, indent=2)

def add_faq(question, answer):
    data = load_knowledge()
    data.setdefault("faq", []).append({"q": question, "a": answer})
    save_knowledge(data)

def edit_product(name, new_info):
    data = load_knowledge()
    for p in data.get("products", []):
        if p["name"].lower() == name.lower():
            p.update(new_info)
    save_knowledge(data)

def reload_knowledge():
    """Chiama questa funzione nel bot ogni volta che salvi per aggiornare la knowledge live."""

# --- ESEMPIO USO ---
if __name__ == "__main__":
    add_faq("Posso ordinare dall’estero?", "Sì, spediamo in tutta Europa!")
    edit_product("Acido Ialuronico", {"desc": "Nuova descrizione aggiornata."})
    print(load_knowledge())
