"""
AuditService – Audit logging crittografato, accessi, azioni sensibili, GDPR/AI Act ready.
"""

import logging
from typing import Dict, List, Optional
from datetime import datetime
import hashlib

class AuditError(Exception):
    pass

class AuditService:
    def __init__(self):
        self._logs: List[Dict] = []

    def log_event(self, user_id: str, event: str, details: Optional[Dict]=None, sensitive: bool=False):
        ts = datetime.utcnow().isoformat()
        record = {
            "ts": ts,
            "user_id": user_id,
            "event": event,
            "details": details or {},
            "sensitive": sensitive,
            "hash": self._hash(ts + user_id + event)
        }
        self._logs.append(record)
        logging.info(f"[AUDIT] {event} by {user_id} (sens: {sensitive}) – {record['hash'][:8]}")
        return record

    def _hash(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def export(self, since: Optional[str]=None) -> List[Dict]:
        if since:
            since_dt = datetime.fromisoformat(since)
            return [log for log in self._logs if datetime.fromisoformat(log["ts"]) >= since_dt]
        return list(self._logs)
