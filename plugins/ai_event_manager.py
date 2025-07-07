# /plugins_ai/ai_event_manager.py

import openai
from datetime import datetime

class AIEventManager:
    def __init__(self, api_key):
        openai.api_key = api_key

    def create_event(self, title, date, description, language="it"):
        prompt = (
            f"Organizza un evento community: titolo '{title}', data {date}, descrizione {description}, in lingua {language}. "
            "Genera un invito email, una presentazione breve, 3 reminder e un piano follow-up post-evento."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# event_plugin = AIEventManager(api_key="TUA_OPENAI_KEY")
# event_plan = event_plugin.create_event("AI Day 2025", "2025-09-15", "Un giorno per scoprire tutte le novità AI.")
