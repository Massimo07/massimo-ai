"""
dashboard/admin.py – API e logica dashboard Founder/Owner.
"""
from datetime import datetime
from typing import List, Dict, Optional
from models.user import User
from models.world import World
from models.subscription import Subscription
from models.transaction import Transaction

class DashboardAdminService:
    def __init__(self, db):
        self.db = db  # Collegamento a DB o repository

    def get_stats(self) -> Dict:
        return {
            "utenti_totali": self.db.count(User),
            "mondi_attivi": self.db.count(World, filter={"status": "active"}),
            "abbonamenti": self.db.count(Subscription, filter={"is_active": True}),
            "fatturato": self.db.sum(Transaction, "amount", filter={"status": "success"})
        }

    def search_user(self, query: str) -> List[User]:
        return self.db.search(User, query)

    def manage_world(self, world_id: str, action: str) -> Optional[World]:
        world = self.db.get(World, world_id)
        if not world:
            return None
        if action == "disattiva":
            world.status = "inactive"
        elif action == "attiva":
            world.status = "active"
        self.db.save(world)
        return world

    def list_feedback(self) -> List[Dict]:
        return self.db.list("feedback")  # Puoi collegare direttamente Feedback model
