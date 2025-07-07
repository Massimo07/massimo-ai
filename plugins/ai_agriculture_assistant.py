# /plugins_ai/ai_agriculture_assistant.py

import openai

class AIAgricultureAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def farming_advice(self, crop, location, issue, language="it"):
        prompt = (
            f"Consulente AI per agricoltura. Coltura: {crop}, luogo: {location}, problema: {issue}, lingua {language}. "
            "Suggerisci: strategie, prevenzione, trattamenti, ottimizzazione resa, innovazioni green."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# agri_plugin = AIAgricultureAssistant(api_key="TUA_OPENAI_KEY")
# advice = agri_plugin.farming_advice("pomodori", "Sicilia", "parassiti fogliari")
