# ai_business.py
"""
Business Engine ultra-evoluto: crea business plan, analisi SWOT, roadmap, suggerimenti AI-driven.
Pronto per ogni tipo di mondo creato da Massimo AI.
"""

import openai

class AIBusinessEngine:
    def __init__(self, api_key):
        openai.api_key = api_key

    def business_plan(self, idea, mercato, obiettivi, language="it"):
        prompt = (
            f"Crea un business plan per '{idea}' nel mercato {mercato}, obiettivi: {obiettivi}, lingua {language}. "
            "Includi analisi SWOT, stima ricavi, milestones."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def swot(self, idea, mercato, language="it"):
        prompt = (
            f"Genera analisi SWOT per '{idea}' nel mercato {mercato}, lingua {language}."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
