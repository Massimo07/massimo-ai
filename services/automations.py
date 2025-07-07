"""
services/automations.py – Motore automazioni Massimo AI
Task, workflow, trigger, azioni, plugin, orchestrazione AI, estensibilità totale.
"""
from typing import Dict, Any, Callable, List
from core.logger import massimo_logger

class AutomationService:
    def __init__(self):
        self.automations = []

    def create_automation(self, trigger: str, action: Callable, condition: Callable = None, meta: Dict[str, Any] = None):
        automation = {
            "trigger": trigger,
            "action": action,
            "condition": condition,
            "meta": meta or {}
        }
        self.automations.append(automation)
        massimo_logger.info("Automazione creata", trigger=trigger, action=action.__name__)

    def run(self, trigger: str, context: Dict[str, Any] = None):
        for auto in self.automations:
            if auto["trigger"] == trigger and (not auto["condition"] or auto["condition"](context)):
                auto["action"](context)
                massimo_logger.info("Automazione eseguita", trigger=trigger, action=auto["action"].__name__)

automation_service = AutomationService()

# Esempio:
# from services.automations import automation_service
# automation_service.create_automation("new_user", lambda ctx: print(f"Benvenuto {ctx['user']}!"))
