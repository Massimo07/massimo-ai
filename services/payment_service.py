"""
automation_service.py – Automazioni, workflow, azioni pianificate e trigger.
"""
from datetime import datetime
import uuid

class AutomationService:
    def __init__(self, db):
        self.db = db

    def create_automation(self, owner_id: str, name: str, action: str, trigger: str, params=None, meta=None):
        automation = {
            "id": str(uuid.uuid4()),
            "owner_id": owner_id,"""
payment_service.py – Gestione pagamenti, metodi, ricevute.
"""
from models.transaction import Transaction
from datetime import datetime
import uuid

class PaymentService:
    def __init__(self, db):
        self.db = db

    def create_transaction(self, user_id: str, amount: float, method: str = "stripe", plan: str = "personal", status: str = "success", meta=None):
        transaction = Transaction(
            id=str(uuid.uuid4()),
            user_id=user_id,
            amount=amount,
            method=method,
            plan=plan,
            status=status,
            timestamp=datetime.utcnow(),
            meta=meta or {}
        )
        self.db.save(transaction)
        return transaction

    def get_transaction(self, txn_id: str):
        return self.db.get(Transaction, txn_id)

    def refund_transaction(self, txn_id: str):
        transaction = self.get_transaction(txn_id)
        if transaction:
            transaction.status = "refunded"
            self.db.save(transaction)
        return transaction

            "name": name,
            "action": action,
            "trigger": trigger,
            "params": params or {},
            "meta": meta or {},
            "status": "active",
            "created_at": datetime.utcnow()
        }
        self.db.save_automation(automation)
        return automation

    def get_automation(self, automation_id: str):
        return self.db.get_automation(automation_id)

    def deactivate_automation(self, automation_id: str):
        automation = self.get_automation(automation_id)
        if automation:
            automation["status"] = "inactive"
            self.db.save_automation(automation)
        return automation
