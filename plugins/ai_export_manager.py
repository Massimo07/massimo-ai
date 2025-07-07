# /plugins_ai/ai_export_manager.py

import openai

class AIExportManager:
    def __init__(self, api_key):
        openai.api_key = api_key

    def export_strategy(self, product, target_country, language="it"):
        prompt = (
            f"Prepara una strategia export per il prodotto '{product}' verso {target_country}, lingua {language}. "
            "Suggerisci: analisi mercato, requisiti doganali, adattamento etichette, rischi, suggerimenti pratici."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# export_plugin = AIExportManager(api_key="TUA_OPENAI_KEY")
# export_plan = export_plugin.export_strategy("Integratore naturale", "Germania")
