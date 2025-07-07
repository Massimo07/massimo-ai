"""
Onboarding – Flussi avanzati di onboarding agenti/utenti.
Audit, logging, plug-in ready, personalizzazione step e feedback.
"""

from typing import List, Dict, Any, Optional
import logging

class OnboardingFlow:
    """
    Gestisce il flusso di onboarding agenti o utenti.
    """
    def __init__(self, steps: Optional[List[str]] = None):
        self.steps = steps or ["welcome", "setup", "training", "finalize"]
        self.current_step = 0

    def start(self):
        logging.info("[Onboarding] Flusso di onboarding avviato.")
        self.current_step = 0

    def next_step(self) -> str:
        if self.current_step < len(self.steps):
            step = self.steps[self.current_step]
            logging.info(f"[Onboarding] Step corrente: {step}")
            self.current_step += 1
            return step
        logging.info("[Onboarding] Flusso completato.")
        return "done"

    def get_status(self) -> Dict[str, Any]:
        status = {
            "current": self.current_step,
            "total": len(self.steps),
            "steps": self.steps,
            "completed": self.current_step >= len(self.steps),
        }
        logging.info(f"[Onboarding] Stato attuale: {status}")
        return status
