# /plugins_ai/ai_youtube_optimizer.py

import openai

class AIYouTubeOptimizer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def optimize_channel(self, channel_info, language="it"):
        prompt = (
            f"Ottimizza il canale YouTube:\n{channel_info}\n"
            "Suggerisci: idee video virali, titoli, descrizioni, tag, script per intro/outro, orario pubblicazione, trend."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# yt_plugin = AIYouTubeOptimizer(api_key="TUA_OPENAI_KEY")
# yt_ottimizzazione = yt_plugin.optimize_channel("MassimoAI: AI evolutiva per tutti, 10k iscritti, pubblico europeo")
