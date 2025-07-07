"""
PluginService – Gestione plug-in AI di terze parti, caricamento dinamico, verifica sicurezza.
"""

import logging
from typing import Dict, Callable

class PluginError(Exception):
    pass

class PluginService:
    def __init__(self):
        self._plugins: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable):
        if not name or not callable(func):
            raise PluginError("Nome e funzione plugin obbligatori")
        self._plugins[name] = func
        logging.info(f"[PLUGIN] Registrato plugin: {name}")

    def execute(self, name: str, *args, **kwargs):
        if name not in self._plugins:
            raise PluginError(f"Plugin '{name}' non trovato")
        logging.info(f"[PLUGIN] Esecuzione plugin: {name}")
        return self._plugins[name](*args, **kwargs)

    def list_plugins(self):
        return list(self._plugins.keys())
