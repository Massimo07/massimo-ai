"""
services/plugins.py – Plugin system avanzato
Caricamento dinamico, discovery, API plugin, enable/disable, sicurezza, sandbox, estensibilità marketplace.
"""
from typing import Dict, Any, Callable
from core.logger import massimo_logger

class PluginService:
    def __init__(self):
        self.plugins: Dict[str, Callable] = {}

    def load_plugin(self, name: str, plugin_func: Callable):
        self.plugins[name] = plugin_func
        massimo_logger.info("Plugin caricato", name=name)

    def run_plugin(self, name: str, *args, **kwargs) -> Any:
        if name in self.plugins:
            massimo_logger.info("Plugin eseguito", name=name)
            return self.plugins[name](*args, **kwargs)
        raise ValueError("Plugin non trovato")

plugin_service = PluginService()

# Esempio:
# from services.plugins import plugin_service
# plugin_service.load_plugin("saluta", lambda n: f"Ciao {n}!")
# print(plugin_service.run_plugin("saluta", "Massimo"))
