"""
Generator – Modulo per la generazione dinamica di agenti, task, workflow o modelli.
Batch, logging e plug-in ready.
"""

from .custom_agent import CustomAgent
from .base import BaseAgent
from typing import List, Dict, Any
import logging

class AgentGenerator:
    """
    Generatore dinamico di agenti plug-in per workflow e testing massivo.
    """
    @staticmethod
    def generate_agents(agent_specs: List[Dict[str, Any]]) -> List[BaseAgent]:
        agents = []
        for spec in agent_specs:
            agent_type = spec.get("type", "custom")
            if agent_type == "custom":
                agent = CustomAgent(
                    agent_id=spec["id"],
                    name=spec["name"],
                    specialty=spec.get("specialty", "general"),
                    skillset=spec.get("skillset", {}),
                )
            else:
                agent = BaseAgent(agent_id=spec["id"], name=spec["name"], skillset=spec.get("skillset", {}))
            agents.append(agent)
            logging.info(f"[AgentGenerator] Generato agente: {agent.agent_id} ({agent.name})")
        return agents
