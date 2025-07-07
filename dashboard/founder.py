"""
Massimo AI – Founder Dashboard
Pannello founder: controllo assoluto su utenti, mondi, abbonamenti, revenue, plugin, branding, API, backup.
"""
import datetime

class FounderDashboard:
    def __init__(self):
        self.users = {}
        self.worlds = {}
        self.revenue = 0
        self.events = []

    def update_users(self, users):
        self.users = users

    def update_worlds(self, worlds):
        self.worlds = worlds

    def add_revenue(self, amount):
        self.revenue += amount

    def log_event(self, event):
        self.events.append({"time": datetime.datetime.now().isoformat(), **event})

    def report(self):
        return {
            "users": len(self.users),
            "worlds": len(self.worlds),
            "revenue": self.revenue,
            "events": self.events[-50:]
        }
