# /plugins_ai/ai_gamification_engine.py

import openai

class AIGamificationEngine:
    def __init__(self, api_key):
        openai.api_key = api_key

    def gamify(self, context, type="corso", language="it"):
        prompt = (
            f"Gamifica l’esperienza '{context}' ({type}), in lingua {language}. "
            "Suggerisci: 3 missioni, badge con nome e descrizione, livelli di avanzamento, sistema di punteggio, ricompense."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# gamification_plugin = AIGamificationEngine(api_key="TUA_OPENAI_KEY")
# gamification_plan = gamification_plugin.gamify("Corso su leadership AI")
