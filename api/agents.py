from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from pydantic import BaseModel
import logging

router = APIRouter()

class Agent(BaseModel):
    id: int
    name: str

agents_db = {}

@router.post("/", response_model=Agent, status_code=status.HTTP_201_CREATED)
async def create_agent(agent: Agent):
    if agent.id in agents_db:
        logging.warning(f"Agent creation failed: ID {agent.id} already exists")
        raise HTTPException(status_code=400, detail="Agent already exists")
    agents_db[agent.id] = agent
    logging.info(f"Agent created: {agent.id}")
    return agent

@router.get("/", response_model=List[Agent])
async def list_agents(skip: int = 0, limit: int = Query(100, le=100)):
    logging.debug(f"Listing agents: skip {skip}, limit {limit}")
    return list(agents_db.values())[skip:skip+limit]

@router.get("/{agent_id}", response_model=Agent)
async def get_agent(agent_id: int):
    agent = agents_db.get(agent_id)
    if not agent:
        logging.warning(f"Agent not found: ID {agent_id}")
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent
