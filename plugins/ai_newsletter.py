# ai_newsletter.py
"""
Newsletter AI Engine: crea newsletter personalizzate, segmenta target, analizza performance e suggerisce follow-up.
Perfetto per mondi business, community, corsi, vendita prodotti e più.
"""

import openai

class AINewsletterEngine:
    def __init__(self, api_key):
        self.api_key = api_key

    def create_newsletter(self, topic, audience, language="it"):
        prompt = (
            f"Crea una newsletter coinvolgente sul tema '{topic}', pubblico: {audience}, lingua: {language}. "
            "Aggiungi titolo, 3 sezioni, call to action e preview per email."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def analyze_performance(self, stats, language="it"):
        prompt = (
            f"Analizza queste statistiche newsletter:\n{stats}\n"
            "Suggerisci come migliorare apertura, click, conversione, lingua: {language}."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
