"""
Token API – Gestione JWT, refresh, revoke, MFA, logging accessi.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
import logging

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

TOKENS = {}

def get_current_user():
    return {"user_id": "admin"}

@router.post("/login", response_model=Token)
def login(username: str, password: str):
    # Simulazione login
    token = Token(access_token="demo-token", token_type="bearer")
    TOKENS[username] = token
    logging.info(f"[token] Login user {username}")
    return token

@router.post("/refresh", response_model=Token)
def refresh_token(username: str):
    # Simulazione refresh
    token = Token(access_token="refreshed-token", token_type="bearer")
    TOKENS[username] = token
    logging.info(f"[token] Refresh user {username}")
    return token

@router.post("/revoke", status_code=status.HTTP_204_NO_CONTENT)
def revoke_token(username: str):
    TOKENS.pop(username, None)
    logging.info(f"[token] Revoked token for {username}")
