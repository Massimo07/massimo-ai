"""
AgentManager – Gestione centralizzata di tutti gli agenti (CRUD, training, audit, batch).
"""

from .base import BaseAgent
from typing import Dict, Optional, List
import logging

class AgentManager:
    """
    Gestore degli agenti Massimo AI.
    """
    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}

    def register_agent(self, agent: BaseAgent):
        self.agents[agent.agent_id] = agent
        logging.info(f"[AgentManager] Registrato agente {agent.agent_id}")

    def remove_agent(self, agent_id: str):
        if agent_id in self.agents:
            del self.agents[agent_id]
            logging.info(f"[AgentManager] Rimosso agente {agent_id}")

    def get_agent(self, agent_id: str) -> Optional[BaseAgent]:
        return self.agents.get(agent_id)

    def batch_update_agents(self, agent_ids: List[str], update_data: dict):
        for agent_id in agent_ids:
            agent = self.get_agent(agent_id)
            if agent:
                agent.update_skillset(update_data)
                logging.info(f"[AgentManager] Batch updated agent {agent_id}")

    def train_agent(self, agent_id: str, training_data: dict):
        agent = self.get_agent(agent_id)
        if agent:
            agent.log_action("train", training_data)
            logging.info(f"[AgentManager] Training agent {agent_id} con dati {training_data}")
