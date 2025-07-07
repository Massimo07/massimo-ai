# ai_engine/plugins.py
"""
PLUGINS – Registry plug-in AI (Massimo AI)

- Registry dinamico modelli AI (gpt-4o, claude, custom…)
- Auto-discovery e plug-in system
- Logging ogni registrazione/override
"""

from ai_engine.logging import ai_logger

PLUGINS = {}

def register_plugin(name: str, func):
    """Registra una nuova AI nel registry."""
    PLUGINS[name] = func
    ai_logger.info(f"[plugins] Plugin {name} registrato.")

def get_plugin(name: str):
    """Recupera una AI plugin registrata."""
    return PLUGINS.get(name, None)

def get_all_plugins():
    """Restituisce tutti i plugin registrati."""
    return list(PLUGINS.keys())

# Esempi default
def _gpt_4o_plugin(input_data):
    return f"Risposta GPT-4o: {input_data.get('prompt','')}".strip()

def _claude_plugin(input_data):
    return f"Risposta Claude: {input_data.get('prompt','')}".strip()

# Autoregistra default all’avvio
register_plugin("gpt-4o", _gpt_4o_plugin)
register_plugin("claude", _claude_plugin)
