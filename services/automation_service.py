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
            "owner_id": owner_id,
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
