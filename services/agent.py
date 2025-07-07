# /services/agent.py

def create_agent(world_id, name, skills, db):
    agent_id = f"agent_{len(db['agents'])+1}"
    db["agents"][agent_id] = {
        "id": agent_id,
        "world_id": world_id,
        "name": name,
        "skills": skills,
        "status": "active",
    }
    db["worlds"][world_id].setdefault("agents", []).append(agent_id)
    return db["agents"][agent_id]

def list_agents(world_id, db):
    agent_ids = db["worlds"][world_id].get("agents", [])
    return [db["agents"][a] for a in agent_ids]

def assign_agent(world_id, agent_id, task, db):
    db["agents"][agent_id].setdefault("tasks", []).append(task)
    return db["agents"][agent_id]
