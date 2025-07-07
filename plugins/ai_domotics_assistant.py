# /plugins_ai/ai_domotics_assistant.py

import openai

class AIDomoticsAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def suggest_routine(self, house_type, needs, language="it"):
        prompt = (
            f"Sei un esperto AI di domotica per {house_type}. Necessità: {needs}, lingua {language}. "
            "Suggerisci: automazioni smart per sicurezza, risparmio energetico, comfort, esempi di routine."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# domotics_plugin = AIDomoticsAssistant(api_key="TUA_OPENAI_KEY")
# automazioni = domotics_plugin.suggest_routine("appartamento", "risparmiare energia e sicurezza")
