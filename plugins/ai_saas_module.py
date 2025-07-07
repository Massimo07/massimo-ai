# /plugins_ai/ai_saas_module.py

import openai

class AISaasModule:
    def __init__(self, api_key):
        openai.api_key = api_key

    def design_saas(self, feature_set, target, language="it"):
        prompt = (
            f"Progetta un modulo SaaS: funzionalità richieste: {feature_set}, target: {target}, lingua {language}. "
            "Suggerisci architettura, onboarding, strategie di prezzo, upsell/cross-sell, sicurezza dati."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# saas_plugin = AISaasModule(api_key="TUA_OPENAI_KEY")
# design = saas_plugin.design_saas("gestione documenti AI, API pubblica", "PMI e startup tech")
