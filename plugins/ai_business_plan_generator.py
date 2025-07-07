# /plugins_ai/ai_business_plan_generator.py

import openai

class AIBusinessPlanGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_plan(self, idea, target_market, goal, language="it"):
        prompt = (
            f"Genera un business plan completo per l’idea: '{idea}', mercato target: {target_market}, obiettivo: {goal}, lingua {language}. "
            "Includi: sintesi progetto, analisi SWOT, clienti ideali, competitor, canali, marketing, stima ricavi, roadmap 12 mesi."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# bp_plugin = AIBusinessPlanGenerator(api_key="TUA_OPENAI_KEY")
# business_plan = bp_plugin.generate_plan("App per AI personalizzata", "Europa", "Scalabilità SaaS")
