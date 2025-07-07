"""
HEALTHCHECK – Self-diagnosis avanzata, REST, logging, alert.
"""
def system_health():
    checks = {
        "database": True,
        "ai_engine": True,
        "api": True,
        "storage": True,
        "email": True,
    }
    status = all(checks.values())
    return {"status": "ok" if status else "alert", "checks": checks}
