# /plugins_ai/ai_event_booster.py

import openai

class AIEventBooster:
    def __init__(self, api_key):
        openai.api_key = api_key

    def boost_event(self, event_desc, target, language="it"):
        prompt = (
            f"Agisci come AI booster per eventi. Evento: {event_desc}, target: {target}, lingua {language}. "
            "Suggerisci: idee creative, strategie marketing, gestione ospiti, follow-up post evento, report finale."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# booster_plugin = AIEventBooster(api_key="TUA_OPENAI_KEY")
# result = booster_plugin.boost_event("Festival Innovazione AI", "imprenditori under 40")
