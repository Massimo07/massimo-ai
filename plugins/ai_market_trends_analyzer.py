# /plugins_ai/ai_market_trends_analyzer.py

import openai

class AIMarketTrendsAnalyzer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_trends(self, sector, period="12 mesi", language="it"):
        prompt = (
            f"Analizza i trend di mercato nel settore: {sector}, periodo: {period}, lingua {language}. "
            "Suggerisci nicchie emergenti, rischi, opportunità e nuovi business possibili."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# trends_plugin = AIMarketTrendsAnalyzer(api_key="TUA_OPENAI_KEY")
# report = trends_plugin.analyze_trends("AI per salute", "24 mesi")
