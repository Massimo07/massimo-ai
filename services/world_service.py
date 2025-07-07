"""
world_service.py – Gestione mondi AI generati, branding, owner, features.
"""
from models.world import World
import uuid
from datetime import datetime

class WorldService:
    def __init__(self, db):
        self.db = db

    def create_world(self, name: str, creator_id: str, price: float = 0.0, branding=None, features=None, meta=None):
        world = World(
            id=str(uuid.uuid4()),
            name=name,
            creator_id=creator_id,
            price=price,
            branding=branding or {},
            features=features or [],
            status="active",
            created_at=datetime.utcnow(),
            meta=meta or {}
        )
        self.db.save(world)
        return world

    def get_world(self, world_id: str):
        return self.db.get(World, world_id)

    def update_world(self, world_id: str, **kwargs):
        world = self.get_world(world_id)
        if not world:
            return None
        for k, v in kwargs.items():
            setattr(world, k, v)
        self.db.save(world)
        return world

    def deactivate_world(self, world_id: str):
        world = self.get_world(world_id)
        if world:
            world.status = "inactive"
            self.db.save(world)
        return world
