"""
dashboard/user.py – Gestione avanzata utenti da dashboard founder/admin.
"""
from models.user import User

class DashboardUserService:
    def __init__(self, db):
        self.db = db

    def list_users(self, limit: int = 100):
        return self.db.list(User, limit=limit)

    def block_user(self, user_id: str):
        user = self.db.get(User, user_id)
        if user:
            user.is_active = False
            self.db.save(user)
            return True
        return False

    def reactivate_user(self, user_id: str):
        user = self.db.get(User, user_id)
        if user:
            user.is_active = True
            self.db.save(user)
            return True
        return False

    def assign_role(self, user_id: str, role: str):
        user = self.db.get(User, user_id)
        if user:
            user.role = role
            self.db.save(user)
            return True
        return False
