"""
Orchestrator – Gestione avanzata di workflow tra agenti, task e decisioni.
Batch, plug-in, error handling e logging.
"""

import logging
from typing import List, Any, Dict
from .base import BaseAgent

class Orchestrator:
    """
    Orchestratore per agenti e task multipli.
    """
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents

    def run_workflow(self, data: Any) -> List[Any]:
        """
        Esegue una catena di agenti su dati in ingresso.
        """
        results = []
        for agent in self.agents:
            try:
                output = agent.act(data)
                results.append(output)
                logging.info(f"[Orchestrator] Agent {agent.agent_id} ({agent.name}) ha processato: {output}")
            except Exception as e:
                logging.error(f"[Orchestrator] Errore su {agent.agent_id}: {e}")
        return results

    def summary(self) -> Dict[str, Any]:
        info = {
            "total_agents": len(self.agents),
            "agent_names": [a.name for a in self.agents],
        }
        logging.info(f"[Orchestrator] Sommario: {info}")
        return info
