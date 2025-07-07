"""
TrainingAgent – Gestione avanzata di training, feedback, RLHF, log e miglioramento continuo degli agenti.
Audit, plug-in, recovery, metriche.
"""

import logging
from typing import Any, Dict, List

class TrainingAgent:
    """
    Gestisce training agenti AI/umani, log performance, feedback e recovery.
    """
    def __init__(self, name: str = "TrainingAgent"):
        self.name = name
        self.training_log: List[Dict[str, Any]] = []

    def train(self, agent_id: str, data: Dict[str, Any]):
        entry = {"agent_id": agent_id, "data": data}
        self.training_log.append(entry)
        logging.info(f"[TrainingAgent] Training per {agent_id} – DATA: {data}")

    def feedback(self, agent_id: str, feedback_data: Dict[str, Any]):
        entry = {"agent_id": agent_id, "feedback": feedback_data}
        self.training_log.append(entry)
        logging.info(f"[TrainingAgent] Feedback per {agent_id} – DATA: {feedback_data}")

    def get_training_history(self) -> List[Dict[str, Any]]:
        return self.training_log

    def explain(self) -> str:
        return f"{self.name} traccia e migliora costantemente le performance degli agenti tramite training e feedback."
