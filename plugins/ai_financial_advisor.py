# /plugins_ai/ai_financial_advisor.py

import openai

class AIFinancialAdvisor:
    def __init__(self, api_key):
        openai.api_key = api_key

    def advise(self, user_profile, goal, language="it"):
        prompt = (
            f"Agisci come advisor AI per finanza personale. Profilo utente: {user_profile}, obiettivo: {goal}, lingua {language}. "
            "Suggerisci: piani di risparmio, controllo spese, simulazione investimento base, avvertenze e disclaimer."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# fin_plugin = AIFinancialAdvisor(api_key="TUA_OPENAI_KEY")
# plan = fin_plugin.advise("studente, 25 anni, entrate 900 euro/mese", "comprare casa")
