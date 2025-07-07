"""
Massimo AI – Auditing
Traccia ogni azione utente, agente, API per compliance, debugging, privacy.
"""
import datetime

class AuditLog:
    def __init__(self):
        self.entries = []

    def log(self, user_id, action, meta=None):
        entry = {
            "time": datetime.datetime.utcnow().isoformat(),
            "user": user_id,
            "action": action,
            "meta": meta or {},
        }
        self.entries.append(entry)

    def export(self, format="json"):
        if format == "json":
            import json
            return json.dumps(self.entries)
        if format == "csv":
            import csv, io
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=self.entries[0].keys())
            writer.writeheader()
            writer.writerows(self.entries)
            return output.getvalue()
