# /plugins_ai/ai_conversational_dashboard.py

import openai

class AIConversationalDashboard:
    def __init__(self, api_key):
        openai.api_key = api_key

    def dashboard_query(self, query, language="it"):
        prompt = (
            f"Rispondi come dashboard conversazionale, query: '{query}', lingua {language}. "
            "Suggerisci insight chiave, genera descrizione di grafici, suggerisci azioni da intraprendere."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# dashboard_plugin = AIConversationalDashboard(api_key="TUA_OPENAI_KEY")
# risposta = dashboard_plugin.dashboard_query("Quali sono i 3 canali che generano più iscrizioni?")
