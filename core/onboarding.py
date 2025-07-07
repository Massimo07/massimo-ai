"""
ONBOARDING – Percorsi step dinamici, tracking, feedback, quiz.
"""
from typing import Dict, List

def onboarding_steps(user_id: int) -> List[Dict]:
    return [
        {"step": 1, "desc": "Benvenuto!", "completed": False},
        {"step": 2, "desc": "Compila il profilo.", "completed": False},
        {"step": 3, "desc": "Quiz iniziale.", "completed": False}
    ]

def record_onboarding_step(user_id: int, step: int, data: Dict):
    # TODO: salvataggio su DB/log
    print(f"[ONBOARDING] {user_id} step {step} data {data}")
