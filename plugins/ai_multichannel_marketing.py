# /plugins_ai/ai_multichannel_marketing.py

import openai

class AIMultichannelMarketing:
    def __init__(self, api_key):
        openai.api_key = api_key

    def plan_campaign(self, product, channels, budget, language="it"):
        prompt = (
            f"Pianifica una campagna marketing multicanale per il prodotto: {product}, canali: {channels}, budget: {budget}, lingua {language}. "
            "Suggerisci: idea creativa, strategia, tempistiche, allocazione budget, KPI da tracciare."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# mcm_plugin = AIMultichannelMarketing(api_key="TUA_OPENAI_KEY")
# campagna = mcm_plugin.plan_campaign("Massimo AI Pro", ["TikTok", "LinkedIn", "email", "WhatsApp"], "3000 euro")
