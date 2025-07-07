"""
Entrypoint principale di Massimo AI Universal Mind.
Avvia tutti i servizi, plugin, monitoring, federation, logging.
"""

import logging
from core.config import settings
from core.plugin_engine import PluginEngine
from core.federation import FederationEngine
from core.monitoring import start_monitoring
from core.error_handlers import register_error_handlers
from core.logging import setup_logging

def bootstrap():
    setup_logging()
    register_error_handlers()
    start_monitoring()

    plugin_engine = PluginEngine()
    plugin_engine.load_all_plugins()

    federation_engine = FederationEngine(plugin_engine)
    print("Massimo AI Universal Mind è ONLINE!")

    try:
        while True:
            federation_engine.maintain_mesh()
            plugin_engine.hot_reload_check()
    except KeyboardInterrupt:
        print("Chiusura Massimo AI Universal Mind")

if __name__ == "__main__":
    bootstrap()
