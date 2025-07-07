# /plugins_ai/ai_customer_support.py

import openai

class AICustomerSupport:
    def __init__(self, api_key):
        openai.api_key = api_key

    def suggest_response(self, message, language="it"):
        prompt = (
            f"Rispondi come customer support esperto, in lingua {language}, al seguente messaggio utente:\n{message}\n"
            "Suggerisci una risposta empatica e professionale, con soluzione pratica e chiusura positiva."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# support_plugin = AICustomerSupport(api_key="TUA_OPENAI_KEY")
# reply = support_plugin.suggest_response("Non riesco ad accedere al corso, potete aiutarmi?")
