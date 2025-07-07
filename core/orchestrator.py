"""
Massimo AI – Orchestrator Module
Governa tutti i mondi AI, agent, servizi. Auto-healing, logging, scaling. 
Massima resilienza e flessibilità, pronto per ambienti cloud-native.
"""
import logging
from services.notify import Notifier
from services.healthcheck import HealthCheck
from services.auto_scaler import AutoScaler
from dashboard.founder import FounderDashboard

class Orchestrator:
    def __init__(self):
        self.logger = logging.getLogger("Orchestrator")
        self.healthcheck = HealthCheck()
        self.scaler = AutoScaler()
        self.notifier = Notifier()
        self.dashboard = FounderDashboard()
        self.worlds = {}

    def register_world(self, world):
        self.logger.info(f"Registering new world: {world.name}")
        self.worlds[world.id] = world
        self.dashboard.update_worlds(self.worlds)

    def monitor(self):
        """Controlla salute mondi e agent, auto-healing se serve."""
        for world_id, world in self.worlds.items():
            if not self.healthcheck.check(world):
                self.logger.warning(f"World {world_id} unhealthy! Restarting...")
                world.restart()
                self.notifier.critical(f"World {world_id} auto-restarted!")
        self.scaler.adapt_resources(self.worlds)

    def audit_log(self, action, user_id, meta=None):
        """Traccia azione, user, meta, audit trail reale."""
        log_entry = {
            "action": action, "user": user_id, "meta": meta
        }
        self.logger.info(f"AUDIT: {log_entry}")
        self.dashboard.log_event(log_entry)
