# ai_marketing.py
"""
Marketing AI Engine: genera strategie multi-canale, campagne, funnel, copy per ADV, email, TikTok, WhatsApp, Instagram, Telegram.
Ottimizzato per performance e engagement.
"""

import openai

class AIMarketingEngine:
    def __init__(self, api_key):
        openai.api_key = api_key

    def campaign(self, product, channels, budget, language="it"):
        prompt = (
            f"Pianifica una campagna marketing per '{product}', canali: {channels}, budget: {budget}, lingua {language}. "
            "Includi strategia creativa, fasi, KPI e suggerimenti AI."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def social_copy(self, topic, platform, language="it"):
        prompt = (
            f"Scrivi un post ad alto impatto per '{platform}', tema '{topic}', lingua {language}. "
            "Aggiungi CTA, 3 hashtag e tono virale."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
