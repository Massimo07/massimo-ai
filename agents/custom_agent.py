"""
CustomAgent – Esempio di agente personalizzato, completamente plug-in ready.
Dimostra override di act, logging, explain e skillset custom.
"""

from .base import BaseAgent
from typing import Any, Dict

class CustomAgent(BaseAgent):
    """
    Agente custom con comportamento avanzato.
    """
    def __init__(self, agent_id: str, name: str, specialty: str, skillset: Dict[str, Any] = None):
        super().__init__(agent_id, name, skillset)
        self.specialty = specialty

    def act(self, data: Any) -> Any:
        result = f"CustomAgent {self.name} ({self.specialty}) processa: {data}"
        self.log_action("custom_act", {"input": data, "result": result})
        return result

    def explain(self) -> Dict[str, str]:
        explanation = f"CustomAgent {self.name} specializzato in {self.specialty} con skillset {list(self.skillset.keys())}."
        self.log_action("custom_explain", {"explanation": explanation})
        return {"explanation": explanation}
