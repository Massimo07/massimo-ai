# /plugins_ai/ai_community_analytics.py

import openai

class AICommunityAnalytics:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_messages(self, messages, language="it"):
        prompt = (
            f"Analizza questi messaggi della community (in lingua {language}):\n"
            f"{messages}\n"
            "Identifica: trend, argomenti caldi, sentiment prevalente, suggerimenti AI per migliorare la community."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# analytics_plugin = AICommunityAnalytics(api_key="TUA_OPENAI_KEY")
# report = analytics_plugin.analyze_messages(["Ciao a tutti!", "Grande Massimo AI!", "Come posso trovare nuovi clienti?"])
