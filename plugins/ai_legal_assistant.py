# /plugins_ai/ai_legal_assistant.py

import openai

class AILegalAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def legal_advice(self, question, country="Italia", language="it"):
        prompt = (
            f"Rispondi come assistente legale, Paese: {country}, lingua {language}. "
            f"Domanda: {question}\n"
            "Se puoi, suggerisci anche modello di contratto o riferimento legale utile."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# legal_plugin = AILegalAssistant(api_key="TUA_OPENAI_KEY")
# advice = legal_plugin.legal_advice("Come si tutela la privacy per un corso online?")
