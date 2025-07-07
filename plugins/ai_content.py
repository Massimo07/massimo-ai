# ai_content.py
"""
Content Factory AI: crea contenuti per blog, social, email, slide, podcast, video.
Usa prompt evoluti e personalizzabili. Pronto per tutti i mondi verticali.
"""

import openai

class AIContentFactory:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_content(self, format, topic, audience, language="it"):
        prompt = (
            f"Genera contenuto formato {format} su '{topic}' per pubblico {audience}, lingua {language}. "
            "Includi CTA e suggerimenti originali."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def generate_slide_deck(self, topic, n_slide=7, language="it"):
        prompt = (
            f"Crea una presentazione di {n_slide} slide sul tema '{topic}', lingua {language}. "
            "Usa titolo efficace e punti chiave."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
