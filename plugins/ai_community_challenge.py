# /plugins_ai/ai_community_challenge.py

import json
from datetime import datetime

class AICommunityChallenge:
    def __init__(self, challenge_file="challenges.json"):
        self.challenge_file = challenge_file

    def create_challenge(self, title, description, deadline):
        challenge = {
            "title": title,
            "description": description,
            "deadline": deadline,
            "created": str(datetime.now()),
            "participants": []
        }
        self._log(challenge)
        return {"msg": "Challenge creata!", "challenge": challenge}

    def add_participant(self, challenge_title, user_id):
        # Logica base: append in file (da ottimizzare con DB per sistemi grandi)
        pass  # Da completare con ricerca e update challenge nel file

    def _log(self, data):
        try:
            with open(self.challenge_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(data, ensure_ascii=False) + "\n")
        except Exception as e:
            print("Errore log challenge:", e)

# USO:
# challenge_plugin = AICommunityChallenge()
# challenge_plugin.create_challenge("24h Kindness", "Fai almeno 1 azione gentile in 24 ore!", "2025-08-01")
