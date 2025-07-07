# /plugins_ai/ai_monetization_optimizer.py

import openai

class AIMonetizationOptimizer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def suggest_pricing(self, service: str, value_desc: str, competitors: str = ""):
        prompt = (
            f"Analizza il servizio '{service}' descritto così: {value_desc}. "
            f"Concorrenza: {competitors if competitors else 'nessuna'}."
            "Suggerisci il prezzo ideale e possibili offerte per massimizzare il profitto e la soddisfazione del cliente."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# monet_plugin = AIMonetizationOptimizer(api_key="TUA_OPENAI_KEY")
# pricing = monet_plugin.suggest_pricing("Corso VR Leadership", "Corso immersivo VR per sviluppare leadership", "Meta, Udemy, Coursera")
