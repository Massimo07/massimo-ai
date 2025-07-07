# ai_onboarding_voice_video.py
"""
Onboarding evoluto: accoglie ogni utente con messaggi vocali/video, guida step by step, quiz interattivi, registrazione e feedback.
"""

class OnboardingVoiceVideoAI:
    def __init__(self):
        self.steps = ["Benvenuto!", "Tutorial", "Quiz", "Feedback", "Pronto a partire!"]
        self.progress = {}

    def start(self, user_id):
        self.progress[user_id] = 0
        return self.steps[0]

    def next_step(self, user_id):
        self.progress[user_id] += 1
        idx = self.progress[user_id]
        return self.steps[idx] if idx < len(self.steps) else "Onboarding completato!"

    def get_status(self, user_id):
        idx = self.progress.get(user_id, 0)
        return self.steps[idx]
