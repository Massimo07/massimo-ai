# ai_engine/logging.py
"""
LOGGING – Logging dedicato motore AI (Massimo AI)

Log separato per audit trail, debug, compliance.
"""

import logging

ai_logger = logging.getLogger("ai_engine")
if not ai_logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s][%(levelname)s][AI_ENGINE] %(message)s")
    handler.setFormatter(formatter)
    ai_logger.addHandler(handler)
ai_logger.setLevel(logging.INFO)
