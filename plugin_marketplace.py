"""
Modulo: plugin_marketplace.py
Marketplace interno per plugin/skill: ogni membro può installare skill, tool o moduli extra, anche a pagamento, con validazione admin.
"""

import os

PLUGINS = []

def register_plugin(plugin_name, author, description, price=0):
    plugin = {
        "plugin_name": plugin_name,
        "author": author,
        "description": description,
        "price": price,
        "approved": False
    }
    PLUGINS.append(plugin)
    return plugin

def approve_plugin(plugin_name):
    for p in PLUGINS:
        if p["plugin_name"] == plugin_name:
            p["approved"] = True
            return p
    return None

def list_plugins(approved_only=True):
    if approved_only:
        return [p for p in PLUGINS if p["approved"]]
    return PLUGINS

# --- ESEMPIO USO ---
if __name__ == "__main__":
    register_plugin("SuperQuiz", "MarioRossi", "Quiz interattivi avanzati", 10)
    approve_plugin("SuperQuiz")
    print(list_plugins())
