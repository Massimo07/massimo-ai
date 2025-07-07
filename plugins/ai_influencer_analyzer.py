# /plugins_ai/ai_influencer_analyzer.py

import openai

class AIInfluencerAnalyzer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_influencer(self, profile_info, target_market="Italia"):
        prompt = (
            f"Analizza il profilo influencer:\n{profile_info}\n"
            f"Target: {target_market}.\n"
            "Suggerisci: punti di forza, aree di miglioramento, collaborazioni ideali, strategie social vincenti, rischio reputazionale."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# influencer_plugin = AIInfluencerAnalyzer(api_key="TUA_OPENAI_KEY")
# result = influencer_plugin.analyze_influencer("Profilo Instagram: @massimo_ai_official ...", "Italia")
