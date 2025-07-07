# /plugins_ai/ai_good_tracker.py

import json
from datetime import datetime

class AIGoodTracker:
    def __init__(self, log_file="good_actions.json"):
        self.log_file = log_file

    def track_good_action(self, user_id, action_type, description):
        entry = {
            "user_id": user_id,
            "action_type": action_type,
            "description": description,
            "timestamp": str(datetime.now())
        }
        self._log(entry)
        return {"msg": "Azione positiva registrata!", "dettagli": entry}

    def _log(self, entry):
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception as e:
            print("Errore log azioni positive:", e)

# USO:
# good_tracker = AIGoodTracker()
# good_tracker.track_good_action("user_123", "aiuto", "Ha aiutato un collega in difficoltà")
