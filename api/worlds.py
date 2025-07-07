from fastapi import APIRouter, HTTPException, Depends, status, Query
from typing import List, Optional
from pydantic import BaseModel
import logging

router = APIRouter()

class World(BaseModel):
    id: int
    owner_id: int
    name: str

worlds_db = {}

@router.post("/", response_model=World, status_code=status.HTTP_201_CREATED)
async def create_world(world: World):
    if world.id in worlds_db:
        logging.warning(f"World creation failed: ID {world.id} already exists")
        raise HTTPException(status_code=400, detail="World already exists")
    worlds_db[world.id] = world
    logging.info(f"World created: {world.id}")
    return world

@router.get("/", response_model=List[World])
async def list_worlds(owner_id: Optional[int] = None, skip: int = 0, limit: int = Query(100, le=100)):
    logging.debug(f"Listing worlds: owner {owner_id}, skip {skip}, limit {limit}")
    result = list(worlds_db.values())
    if owner_id:
        result = [w for w in result if w.owner_id == owner_id]
    return result[skip:skip+limit]

@router.get("/{world_id}", response_model=World)
async def get_world(world_id: int):
    world = worlds_db.get(world_id)
    if not world:
        logging.warning(f"World not found: ID {world_id}")
        raise HTTPException(status_code=404, detail="World not found")
    return world
