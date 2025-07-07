"""
services/onboarding.py – Onboarding evoluto utenti/AI worlds
Gestisce tutto il flusso: quiz, tutorial, scelte, step, referral, validazione dati, trigger post-onboarding.
"""
from typing import Dict, Any, Optional
from core.logger import massimo_logger

class OnboardingService:
    def __init__(self):
        self.sessions = {}

    def start(self, user_id: str, world_id: Optional[str] = None):
        self.sessions[user_id] = {
            "step": 0,
            "world": world_id,
            "status": "in_progress"
        }
        massimo_logger.info("Onboarding iniziato", user_id=user_id, world_id=world_id)

    def advance(self, user_id: str):
        if user_id not in self.sessions:
            self.start(user_id)
        self.sessions[user_id]["step"] += 1
        return self.sessions[user_id]

    def get_status(self, user_id: str):
        return self.sessions.get(user_id, {"status": "not_started"})

onboarding_service = OnboardingService()

# Esempio:
# from services.onboarding import onboarding_service
# onboarding_service.start("user123", "CoachAI")
