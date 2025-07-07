from fastapi import APIRouter, HTTPException, Depends, status, Query
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr
import logging

router = APIRouter()

class User(BaseModel):
    id: int
    email: EmailStr
    name: str

users_db = {}

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    if user.id in users_db:
        logging.warning(f"User creation failed: ID {user.id} already exists")
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.id] = user
    logging.info(f"User created: {user.id}")
    return user

@router.get("/", response_model=List[User])
async def list_users(skip: int = 0, limit: int = Query(100, le=100)):
    logging.debug(f"Listing users: skip {skip}, limit {limit}")
    return list(users_db.values())[skip:skip+limit]

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        logging.warning(f"User not found: ID {user_id}")
        raise HTTPException(status_code=404, detail="User not found")
    return user
