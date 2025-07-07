"""
Agent – Agente operativo standard di Massimo AI.
Estende BaseAgent, aggiunge explainability e metadati.
"""

from .base import BaseAgent
import logging
from typing import Any, Dict

class Agent(BaseAgent):
    """
    Agente standard, personalizzabile.
    """

    def act(self, data: Any) -> Any:
        """
        Esegue un'azione sull'input e logga il risultato.
        """
        result = f"{self.name} ha processato: {data}"
        self.log_action("act", {"input": data, "result": result})
        return result

    def explain(self) -> Dict[str, str]:
        """
        Spiega in linguaggio naturale come agisce questo agente.
        """
        explanation = f"Agente {self.name}: agisce su dati e restituisce output personalizzati."
        self.log_action("explain", {"explanation": explanation})
        return {"explanation": explanation}
