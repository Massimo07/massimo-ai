"""
Explain – Modulo per la spiegazione trasparente e auditabile delle decisioni degli agenti.
Include logging dettagliato, motivazioni e tracciamento.
"""

import logging
from typing import Dict, Any

class Explain:
    """
    Strumenti di explainability per gli agenti Massimo AI.
    """

    @staticmethod
    def log_decision(agent_id: str, input_data: Any, output_data: Any, rationale: str):
        """
        Logga la decisione di un agente con dettagli e motivazione.
        """
        logging.info(f"[Explain] Agent {agent_id} | Input: {input_data} | Output: {output_data} | Rationale: {rationale}")

    @staticmethod
    def generate_explanation(agent_name: str, rationale: str) -> Dict[str, str]:
        """
        Restituisce una spiegazione in linguaggio naturale.
        """
        explanation = f"L'agente {agent_name} ha preso la decisione basandosi su: {rationale}"
        logging.info(f"[Explain] Explanation generated: {explanation}")
        return {"explanation": explanation}
