"""
Registry – Gestione dinamica e plug-in degli agenti.
Permette registrazione, ricerca e caricamento agenti in modo modulare e scalabile.
"""

from typing import Type, Dict, Optional
import logging

class AgentRegistry:
    """
    Registro plug-in agenti.
    """

    _registry: Dict[str, Type] = {}

    @classmethod
    def register(cls, agent_type: str, agent_class: Type):
        cls._registry[agent_type] = agent_class
        logging.info(f"[Registry] Registered agent type: {agent_type} -> {agent_class}")

    @classmethod
    def get(cls, agent_type: str) -> Optional[Type]:
        return cls._registry.get(agent_type)

    @classmethod
    def list_agents(cls):
        return list(cls._registry.keys())
