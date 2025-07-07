"""
services/factory.py – AI Factory Massimo AI
Crea, clona e personalizza mondi digitali verticali. Branding, regole, onboarding, dashboard, automazioni.
"""
from typing import Dict, Any, Optional
from core.logger import massimo_logger

class WorldFactory:
    def __init__(self):
        self.worlds = {}

    def create_world(self, owner_id: str, config: Dict[str, Any]) -> Dict[str, Any]:
        world_id = config.get("id") or owner_id + "_" + str(len(self.worlds)+1)
        world = {
            "id": world_id,
            "owner": owner_id,
            "name": config.get("name", "New World"),
            "branding": config.get("branding", {}),
            "modules": config.get("modules", []),
            "status": "active"
        }
        self.worlds[world_id] = world
        massimo_logger.info("Creato nuovo mondo AI", world_id=world_id)
        return world

    def get_world(self, world_id: str) -> Optional[Dict[str, Any]]:
        return self.worlds.get(world_id)

    def list_worlds(self, owner_id: Optional[str] = None):
        if owner_id:
            return [w for w in self.worlds.values() if w["owner"] == owner_id]
        return list(self.worlds.values())

world_factory = WorldFactory()

# Esempio:
# from services.factory import world_factory
# nuovo = world_factory.create_world("user123", {"name":"CoachAI"})
