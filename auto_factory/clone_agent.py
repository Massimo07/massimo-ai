
---

### 📂 **auto_factory/clone_agent.py**  
> (Qui la versione “TOP” con logging, batch, audit, versioning, docstring esplicite)

```python
# auto_factory/clone_agent.py
"""
CLONE_AGENT – Utility per clonazione agenti (Massimo AI)

- Clona agenti AI/umani, stato/profilo/personalità inclusi
- Audit trail completo (compliance/AI Act)
- Versioning/parent tracking
- Security: traccia user
- Batch cloning ready
"""

import copy
import uuid
import datetime
import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("auto_factory.clone_agent")

audit_log: List[Dict] = []

def clone_agent(agent: dict, by_user: str = "system") -> dict:
    """
    Clona un agente, assegna nuova ID, parent, versione e registra audit.
    :param agent: dict agente da clonare
    :param by_user: chi richiede la clonazione
    :return: nuovo agente clonato
    """
    new_agent = copy.deepcopy(agent)
    parent_id = agent.get("id", "unknown")
    new_id = str(uuid.uuid4())
    new_version = agent.get("version", 1) + 1

    new_agent.update({
        "id": new_id,
        "parent": parent_id,
        "version": new_version,
        "created_at": datetime.datetime.utcnow().isoformat(),
        "cloned_by": by_user,
    })

    log_entry = {
        "timestamp": new_agent["created_at"],
        "parent_id": parent_id,
        "new_id": new_id,
        "by_user": by_user,
        "version": new_version,
        "action": "clone_agent"
    }
    audit_log.append(log_entry)
    logger.info(f"[Clone] Agente clonato: {log_entry}")
    return new_agent

def clone_agents_batch(agents: List[dict], by_user: str = "system") -> List[dict]:
    """
    Clona una lista di agenti (batch cloning, audit logging).
    """
    return [clone_agent(a, by_user=by_user) for a in agents]

if __name__ == "__main__":
    # Demo singolo
    agent = {
        "id": "agent-001",
        "nome": "Mentor",
        "personality": "coach",
        "history": [],
        "version": 1
    }
    print("Agente di partenza:", agent)
    clone = clone_agent(agent, by_user="mario")
    print("Nuovo agente clonato:", clone)
    print("Audit log:", audit_log)

    # Demo batch
    agents = [
        {"id": "agent-002", "nome": "Sara", "personality": "helper", "version": 2, "history": []},
        {"id": "agent-003", "nome": "Alex", "personality": "advisor", "version": 1, "history": []},
    ]
    clones = clone_agents_batch(agents, by_user="batcher")
    print("Cloni batch:", clones)
    print("Audit log after batch:", audit_log)
