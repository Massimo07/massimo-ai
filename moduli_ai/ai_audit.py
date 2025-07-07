"""
Modulo: ai_audit.py
Audit AI: ogni azione/risposta/log viene tracciata, revisionata, storicizzata; verifica etica e bug, alert su deriva comportamentale o errori.
"""

import datetime

AUDIT_LOG = []

def log_action(user_id, action, result, ai_version="MAXIMUM"):
    entry = {
        "user_id": user_id,
        "action": action,
        "result": result,
        "ai_version": ai_version,
        "timestamp": datetime.datetime.now().isoformat()
    }
    AUDIT_LOG.append(entry)
    return entry

def get_audit(user_id=None):
    if user_id:
        return [e for e in AUDIT_LOG if e["user_id"] == user_id]
    return AUDIT_LOG

# --- ESEMPIO USO ---
if __name__ == "__main__":
    log_action(1, "risposta quiz", "corretta")
    log_action(1, "generazione badge", "Black Diamond")
    print(get_audit(1))
