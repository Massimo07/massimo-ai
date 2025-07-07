"""
Modulo: agents.py
Gestione agenti AI multipli solo per Massimo AI: puoi creare, registrare e usare diverse “personalità” (motivazionale, scettico, radio, supporto tecnico…).
Ogni agente ha il proprio system prompt, tono, modello, lingua, badge.
Routing intelligente in base al contesto/domanda.
"""

from personality import get_personality
from openai_service import ask_massimo

AGENTS = {
    "motivazionale": {
        "name": "Massimo AI Motivazionale",
        "profile": "base",
        "model": "gpt-4"
    },
    "scettico": {
        "name": "Massimo AI Scettico",
        "profile": "scettico",
        "model": "gpt-4"
    },
    "radio": {
        "name": "Radio Speaker AI",
        "profile": "radio",
        "model": "gpt-4"
    },
    "tecnico": {
        "name": "Massimo AI Supporto Tecnico",
        "profile": "tecnico",
        "model": "gpt-4"
    }
    # Aggiungi altre personalità specifiche di Massimo AI qui!
}

def dispatch_agent(agent_key, prompt, user):
    """
    Instrada la richiesta all'agente corretto in base al tipo/contesto.
    """
    agent = AGENTS.get(agent_key, AGENTS["motivazionale"])
    personality = get_personality(agent["profile"])
    system_prompt = personality["system_prompt"]
    # Puoi personalizzare ulteriormente il prompt in base all’utente, livello ecc.
    user_context = {
        "system_prompt": system_prompt,
        "user_level": user.get("level", "base") if user else "base",
        "user_name": user.get("name", "Amico") if user else "Amico"
    }
    response = ask_massimo(prompt, user_context, model=agent["model"])
    return response

def list_agents():
    """Restituisce l’elenco delle personalità disponibili (solo Massimo AI)."""
    return [{"key": k, "name": v["name"]} for k, v in AGENTS.items()]

# --- ESEMPIO USO ---
if __name__ == "__main__":
    # Simula una domanda da utente che vuole motivazione:
    print(dispatch_agent("motivazionale", "Come posso rimanere motivato ogni giorno?", {"level": "primo_passo", "name": "Luca"}))
    # Simula una domanda da scettico:
    print(dispatch_agent("scettico", "Ma funziona davvero Live On Plus?", {"level": "info_free", "name": "Maria"}))
    # Vedi agent disponibili
    print(list_agents())
