"""
Gestisce tutti i plugin/servizi/agent caricabili live.
Permette hot-reload e modularità totale.
"""

import importlib
import os
import logging

class PluginEngine:
    def __init__(self, plugin_dir="services"):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_all_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                modulename = filename[:-3]
                try:
                    module = importlib.import_module(f"{self.plugin_dir}.{modulename}")
                    if hasattr(module, "register_plugin"):
                        self.plugins[modulename] = module.register_plugin()
                        logging.info(f"Caricato plugin: {modulename}")
                except Exception as e:
                    logging.error(f"Errore caricamento plugin {modulename}: {e}")

    def hot_reload_check(self):
        # Da completare con file watcher o reload periodico (consigliato watchdog)
        pass

    def get_plugin(self, name):
        return self.plugins.get(name, None)
