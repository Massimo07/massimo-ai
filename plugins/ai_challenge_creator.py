# ai_challenge_creator.py
"""
Generatore di challenge: crea sfide giornaliere, settimanali, gamificate, per team, community e crescita personale/business.
Include timer, goal, reward, reminder.
"""

import datetime

class AIChallengeCreator:
    def __init__(self):
        self.challenges = []

    def create_challenge(self, name, goal, duration_days, reward):
        challenge = {
            "name": name,
            "goal": goal,
            "duration": duration_days,
            "reward": reward,
            "start": datetime.datetime.now(),
            "completed": False
        }
        self.challenges.append(challenge)
        return challenge

    def complete_challenge(self, idx):
        self.challenges[idx]["completed"] = True
        self.challenges[idx]["end"] = datetime.datetime.now()

    def active_challenges(self):
        return [c for c in self.challenges if not c["completed"]]
