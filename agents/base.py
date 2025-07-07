"""
BaseAgent – Classe astratta di riferimento per tutti gli agenti Massimo AI.
Include logging, audit, skillset e struttura plug-in.
"""

import logging
from typing import Any, Dict, Optional

class BaseAgent:
    """
    Classe base per ogni agente del sistema.
    """
    def __init__(self, agent_id: str, name: str, skillset: Optional[Dict[str, Any]] = None):
        self.agent_id = agent_id
        self.name = name
        self.skillset = skillset or {}
        logging.info(f"[BaseAgent] Creato agente {self.agent_id} ({self.name})")

    def act(self, data: Any) -> Any:
        """
        Azione principale dell'agente – da implementare nelle sottoclassi.
        """
        logging.info(f"[BaseAgent] {self.agent_id} agisce su: {data}")
        return data

    def log_action(self, action: str, info: dict = None):
        """
        Logging e audit di ogni azione importante.
        """
        logging.info(f"[BaseAgent] {self.agent_id} ACTION: {action} | INFO: {info}")

    def update_skillset(self, new_skills: Dict[str, Any]):
        """
        Aggiorna lo skillset dell'agente.
        """
        self.skillset.update(new_skills)
        self.log_action("update_skillset", {"skills": self.skillset})
