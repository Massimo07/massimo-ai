"""
Modulo: ai_dream2action.py
Da sogno a azione: ascolta il tuo sogno/obiettivo, lo traduce in step reali, fissa reminder, invia motivazione ogni settimana per non mollare mai!
"""

import datetime

ACTIONS = {}

def add_goal(user_id, dream):
    start = datetime.date.today()
    steps = [f"Step {i+1} per {dream}" for i in range(4)]
    ACTIONS[user_id] = {"dream": dream, "steps": steps, "pro_]()
