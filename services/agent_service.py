"""
agent_service.py – Gestione agenti AI: creazione, assegnazione, disattivazione.
"""
from models.agent import Agent
import uuid
from datetime import datetime

class AgentService:
    def __init__(self, db):
        self.db = db

    def create_agent(self, owner_id: str, agent_type: str, skills=None, meta=None):
        agent = Agent(
            id=str(uuid.uuid4()),
            owner_id=owner_id,
            agent_type=agent_type,
            skills=skills or [],
            status="active",
            created_at=datetime.utcnow(),
            meta=meta or {}
        )
        self.db.save(agent)
        return agent

    def get_agent(self, agent_id: str):
        return self.db.get(Agent, agent_id)

    def deactivate_agent(self, agent_id: str):
        agent = self.get_agent(agent_id)
        if agent:
            agent.status = "inactive"
            self.db.save(agent)
        return agent
