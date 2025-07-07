# /plugins_ai/ai_personal_finance_tracker.py

import openai

class AIPersonalFinanceTracker:
    def __init__(self, api_key):
        openai.api_key = api_key

    def track_finance(self, incomes, expenses, goals, language="it"):
        prompt = (
            f"Traccia finanze personali. Entrate: {incomes}, Uscite: {expenses}, Obiettivi: {goals}, lingua {language}. "
            "Suggerisci piano risparmio, segnala spese critiche, idee per raggiungere gli obiettivi."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# finance_plugin = AIPersonalFinanceTracker(api_key="TUA_OPENAI_KEY")
# plan = finance_plugin.track_finance("2000€/mese", "900€/mese", "viaggio in USA")
