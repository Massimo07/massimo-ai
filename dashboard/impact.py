"""
Massimo AI – Impact Tracker
Traccia e visualizza impatto positivo generato. Badge, leaderboard, report automatici.
"""
import datetime

class ImpactTracker:
    def __init__(self):
        self.user_actions = {}

    def log_action(self, user_id, action_type):
        now = datetime.datetime.utcnow().isoformat()
        if user_id not in self.user_actions:
            self.user_actions[user_id] = []
        self.user_actions[user_id].append({"type": action_type, "time": now})

    def get_leaderboard(self):
        # Ordina utenti per numero di azioni positive
        sorted_users = sorted(self.user_actions.items(), key=lambda x: len(x[1]), reverse=True)
        return [{"user": uid, "actions": len(actions)} for uid, actions in sorted_users]

    def user_report(self, user_id):
        return self.user_actions.get(user_id, [])
