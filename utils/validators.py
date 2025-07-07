"""
utils/validators.py

Validatori enterprise: email, password, phone, ecc.
"""
import re

def is_valid_email(email: str) -> bool:
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def is_strong_password(pw: str) -> bool:
    return len(pw) >= 8 and any(c.isupper() for c in pw) and any(c.isdigit() for c in pw)
