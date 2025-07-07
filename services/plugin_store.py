v# /services/plugin_store.py

PLUGIN_REGISTRY = {
    "calendar_ai": {
        "name": "CalendarAI",
        "description": "Calendario intelligente con promemoria e pianificazione AI.",
        "category": "productivity",
        "installable_on": ["all"],
        "enabled_by_default": False,
    },
    "chatbot_assistant": {
        "name": "Chatbot Assistant",
        "description": "Chatbot personalizzabile con AI evoluta.",
        "category": "communication",
        "installable_on": ["all"],
        "enabled_by_default": True,
    },
    "voice_to_text": {
        "name": "Voice to Text",
        "description": "Trascrizione vocale avanzata e note audio.",
        "category": "tools",
        "installable_on": ["web", "mobile", "glasses"],
        "enabled_by_default": False,
    },
    # Puoi aggiungere infiniti plugin!
}

def list_plugins(world_type=None):
    # Filtra i plugin per mondo se serve (es: mondi speciali con plugin dedicati)
    if world_type:
        return [p for p in PLUGIN_REGISTRY.values() if world_type in p["installable_on"] or "all" in p["installable_on"]]
    return list(PLUGIN_REGISTRY.values())

def install_plugin(world_id, plugin_key, db):
    if plugin_key not in PLUGIN_REGISTRY:
        raise ValueError("Plugin non esistente")
    db["worlds"][world_id]["plugins"].append(plugin_key)
    return PLUGIN_REGISTRY[plugin_key]
