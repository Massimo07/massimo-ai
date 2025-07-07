"""
user_service.py – Gestione utenti: CRUD, onboarding, sicurezza, ruoli.
"""
from models.user import User
import uuid
from datetime import datetime

class UserService:
    def __init__(self, db):
        self.db = db

    def create_user(self, email: str, name: str, password_hash: str, lang="it", role="user", meta=None):
        user = User(
            id=str(uuid.uuid4()),
            email=email,
            name=name,
            password_hash=password_hash,
            role=role,
            lang=lang,
            created_at=datetime.utcnow(),
            is_active=True,
            meta=meta or {}
        )
        self.db.save(user)
        return user

    def get_user(self, user_id: str):
        return self.db.get(User, user_id)

    def update_user(self, user_id: str, **kwargs):
        user = self.get_user(user_id)
        if not user:
            return None
        for k, v in kwargs.items():
            setattr(user, k, v)
        self.db.save(user)
        return user

    def delete_user(self, user_id: str):
        user = self.get_user(user_id)
        if user:
            user.is_active = False
            self.db.save(user)
        return user
