"""
core/monitoring.py – Metriche, healthcheck, telemetria Prometheus, alert real-time.
"""

import logging
from services.metrics import MetricsService

class MonitoringService:
    def __init__(self):
        self.metrics = MetricsService()

    def health(self):
        # Puoi aggiungere check su DB/API/disk/ML
        logging.info("[MONITOR] Healthcheck OK")
        return {"status": "OK"}

    def export_metrics(self):
        return self.metrics.export()
