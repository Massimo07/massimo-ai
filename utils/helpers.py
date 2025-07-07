import uuid
from datetime import datetime

def generate_uuid():
    return str(uuid.uuid4())

def now_iso():
    return datetime.utcnow().isoformat() + "Z"

def paginate(items, skip: int = 0, limit: int = 100):
    return items[skip: skip + limit]
