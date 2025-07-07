# ai_dashboard.py
"""
Conversational Dashboard AI: report in linguaggio naturale, insight, generazione grafici, KPI spiegati.
Chiedi qualsiasi dato, Massimo AI lo trova e lo racconta.
"""

import openai

class AIDashboard:
    def __init__(self, api_key):
        openai.api_key = api_key

    def insight(self, query, language="it"):
        prompt = (
            f"Rispondi come dashboard conversazionale: query '{query}', lingua {language}. "
            "Suggerisci insight, dati, grafici e azioni suggerite."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def kpi_report(self, area, period, language="it"):
        prompt = (
            f"Crea report KPI per area '{area}', periodo {period}, lingua {language}. "
            "Spiega trend, valori anomali e suggerisci miglioramenti."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
