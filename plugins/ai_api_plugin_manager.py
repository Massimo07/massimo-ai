# ai_api_plugin_manager.py
"""
Manager universale per la gestione, il caricamento e l’orchestrazione di plug-in AI.
Supporta auto-discovery, versioning, loading dinamico e compatibilità multi-mondo.
"""

import os
import importlib

class APIPluginManager:
    def __init__(self, plugin_dir="plugins_ai"):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugins(self):
        """Carica automaticamente tutti i moduli plugin nella cartella."""
        for file in os.listdir(self.plugin_dir):
            if file.endswith(".py") and not file.startswith("__"):
                name = file[:-3]
                module = importlib.import_module(f"{self.plugin_dir}.{name}".replace("/", "."))
                self.plugins[name] = module

    def get_plugin(self, name):
        """Recupera un plugin per nome."""
        return self.plugins.get(name, None)
