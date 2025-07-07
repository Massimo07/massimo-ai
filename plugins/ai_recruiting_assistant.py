# /plugins_ai/ai_recruiting_assistant.py

import openai

class AIRecruitingAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_cv(self, cv_text, role, language="it"):
        prompt = (
            f"Analizza questo CV per la posizione '{role}', in lingua {language}.\n"
            f"CV:\n{cv_text}\n"
            "Riassumi i punti di forza, segnala eventuali punti deboli e proponi 3 domande mirate per il colloquio."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# rec_plugin = AIRecruitingAssistant(api_key="TUA_OPENAI_KEY")
# result = rec_plugin.analyze_cv("CV di Mario Rossi...", "Sales Manager")
