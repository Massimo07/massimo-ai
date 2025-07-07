# tests/test_agents.py
"""
Test agent registry, training, explain
"""

from agents.agent import Agent
from agents.registry import register_agent, find_agent, clear_registry
from agents.training import train_agent

def test_registry_and_training():
    clear_registry()
    a = Agent(nome="Mentor", skillset=["help"], role="AI")
    register_agent(a)
    found = find_agent(nome="Mentor")
    assert found and found[0].nome == "Mentor"
    result = train_agent(a, dataset="motivazionale")
    assert "addestrato" in result
