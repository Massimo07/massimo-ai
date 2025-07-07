"""
UTILS – Helper avanzati, validazioni, batch export, hashing.
"""
import hashlib
from typing import List, Dict

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def is_email_valid(email: str) -> bool:
    return "@" in email and "." in email

def batch_export_csv(data: List[Dict], delimiter: str = ",") -> str:
    if not data:
        return ""
    header = delimiter.join(data[0].keys())
    lines = [header]
    for row in data:
        lines.append(delimiter.join(str(row[k]) for k in row))
    return "\n".join(lines)
