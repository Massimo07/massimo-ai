import logging
from datetime import datetime

GDPR_LOG_FILE = "logs/gdpr.log"

def log_consent(user_id: str, action: str, details: str = ""):
    with open(GDPR_LOG_FILE, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()}Z | user={user_id} | action={action} | {details}\n")

def anonymize_user_data(user_data: dict) -> dict:
    anonymized = user_data.copy()
    for key in ["email", "phone", "address"]:
        if key in anonymized:
            anonymized[key] = "***"
    return anonymized
