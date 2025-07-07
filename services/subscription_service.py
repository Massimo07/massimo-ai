"""
subscription_service.py – Gestione abbonamenti, livelli, scadenze, rinnovi.
"""
from models.subscription import Subscription
from datetime import datetime, timedelta
import uuid

class SubscriptionService:
    def __init__(self, db):
        self.db = db

    def create_subscription(self, user_id: str, plan: str, duration_months=1, payment_method="stripe", meta=None):
        start = datetime.utcnow()
        end = start + timedelta(days=30 * duration_months)
        subscription = Subscription(
            id=str(uuid.uuid4()),
            user_id=user_id,
            plan=plan,
            start_date=start,
            end_date=end,
            is_active=True,
            auto_renew=True,
            payment_method=payment_method,
            meta=meta or {}
        )
        self.db.save(subscription)
        return subscription

    def get_subscription(self, sub_id: str):
        return self.db.get(Subscription, sub_id)

    def cancel_subscription(self, sub_id: str):
        subscription = self.get_subscription(sub_id)
        if subscription:
            subscription.is_active = False
            self.db.save(subscription)
        return subscription
