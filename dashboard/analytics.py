"""
dashboard/analytics.py – Statistiche, grafici, report real-time.
"""
from services.analytics import AnalyticsService

class DashboardAnalytics:
    def __init__(self):
        self.analytics = AnalyticsService()

    def get_events_by_type(self, event_type: str):
        events = self.analytics.report()
        return [e for e in events if e["event"] == event_type]

    def usage_summary(self):
        events = self.analytics.report()
        summary = {}
        for e in events:
            k = e["event"]
            summary[k] = summary.get(k, 0) + 1
        return summary
