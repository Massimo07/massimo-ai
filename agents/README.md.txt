# AGENTS – Massimo AI

## Come usare un agente
```python
from .registry import AgentRegistry
from .founder_assistant import FounderAssistant
agent = FounderAssistant()
agent.set_personality("empathic")
print(agent.answer("Come posso crescere?"))
AgentRegistry.register("founder_assistant", FounderAssistant)
print(agent.get_audit_log())
