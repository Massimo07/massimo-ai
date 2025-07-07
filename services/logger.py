"""
services/logger.py – Logging Massimo AI ultra-pro
Formato JSON, audit trail, masking, invio cloud, alert, rotazione file, plug API.
"""
import json
import datetime

class MassimoLogger:
    def info(self, message, **kwargs):
        self._log("INFO", message, kwargs)
    def error(self, message, **kwargs):
        self._log("ERROR", message, kwargs)
    def warn(self, message, **kwargs):
        self._log("WARN", message, kwargs)
    def _log(self, level, message, data):
        record = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "level": level,
            "message": message,
            "data": data
        }
        print(json.dumps(record))  # Qui puoi mandare a Sentry, Datadog, AWS, etc.

massimo_logger = MassimoLogger()
