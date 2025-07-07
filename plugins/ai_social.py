# ai_social.py
"""
Social AI Engine: genera post, campagne, analisi trend, risposte automatiche.
Ottimo per mondi di branding, community, business e influencer.
"""

import openai

class AISocialEngine:
    def __init__(self, api_key):
        self.api_key = api_key

    def viral_post(self, topic, platform, language="it"):
        prompt = (
            f"Crea un post virale per '{platform}', tema '{topic}', lingua {language}. "
            "Suggerisci copy, CTA, hashtag e orario ideale."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def analyze_trends(self, sector, period="30 giorni", language="it"):
        prompt = (
            f"Analizza i trend social nel settore '{sector}', periodo: {period}, lingua {language}. "
            "Suggerisci opportunità, rischi, idee per community."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
