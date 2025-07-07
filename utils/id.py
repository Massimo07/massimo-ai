"""
utils/id.py – Generatori ID, UUID, hash, random string, custom slug.
"""
import uuid
import secrets
import hashlib

def generate_uuid() -> str:
    """UUID4 random unico globale"""
    return str(uuid.uuid4())

def generate_token(length=32) -> str:
    """Token sicuro per API o sessioni"""
    return secrets.token_urlsafe(length)

def hash_string(s: str) -> str:
    """Hash SHA256 sicuro (es. per idempotenza, deduplica)"""
    return hashlib.sha256(s.encode()).hexdigest()
