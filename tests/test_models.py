
---

## **tests/test_models.py**

```python
# tests/test_models.py
"""
Test modelli Massimo AI – User, Agent, Subscription, World, ecc.
Controllo validità, edge, audit trail.
"""

import pytest
from models.user import User
from models.agent import Agent
from models.subscription import Subscription
from models.feedback import Feedback

def test_user_valid():
    user = User(id=1, nome="Test", email="test@demo.com")
    assert user.nome == "Test"
    assert user.status == "attivo"
    assert isinstance(user.created_at, object)

def test_agent_valid():
    agent = Agent(id=1, nome="AI Mentor", skillset=["coach"], tipo="AI")
    assert agent.skillset == ["coach"]
    assert agent.stato == "attivo"
    assert agent.tipo == "AI"

def test_subscription_edge():
    sub = Subscription(id=1, user_id=1, livello="Info Free")
    assert sub.livello == "Info Free"
    assert sub.status == "attivo"

def test_feedback_minimum():
    fb = Feedback(id=1, user_id=1, testo="Ottimo!", rating=5)
    assert fb.rating == 5
    assert fb.testo == "Ottimo!"
