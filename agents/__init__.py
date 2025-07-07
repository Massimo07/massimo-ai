"""
Modulo agents – Inizializzazione, registry plug-in agenti, auto-discover.
"""

from .base import BaseAgent
from .agent import Agent
from .agent_manager import AgentManager
from .registry import AgentRegistry

# Registry dinamico agenti per plug-in
AGENTS_REGISTRY = {
    "base": BaseAgent,
    "standard": Agent,
}

def get_agent_class(agent_type: str):
    """
    Ritorna la classe agente in base al tipo registrato.
    """
    return AGENTS_REGISTRY.get(agent_type, BaseAgent)
