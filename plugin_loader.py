"""
Modulo: plugin_loader.py
Carica e registra plugin esterni (python file/class) — per skill future, automazioni nuove, estensioni team.
Pronto per il futuro: nessun limite alle possibilità di Massimo AI!
"""

import importlib
import os

PLUGIN_DIR = "plugins/"

def load_plugins():
    plugins = []
    if not os.path.exists(PLUGIN_DIR):
        os.makedirs(PLUGIN_DIR)
    for fname in os.listdir(PLUGIN_DIR):
        if fname.endswith(".py"):
            modname = fname[:-3]
            module = importlib.import_module(f"plugins.{modname}")
            plugins.append(module)
    return plugins

# --- ESEMPIO USO ---
if __name__ == "__main__":
    for plugin in load_plugins():
        print("Caricato plugin:", plugin)
