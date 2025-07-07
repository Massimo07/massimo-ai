# /plugins_ai/ai_newsletter_engine.py

import openai

class AINewsletterEngine:
    def __init__(self, api_key):
        openai.api_key = api_key

    def create_newsletter(self, topic, audience, language="it"):
        prompt = (
            f"Crea una newsletter su '{topic}', pubblico: {audience}, lingua {language}. "
            "Includi: intro, 3 sezioni, call to action, titolo e anteprima."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# nl_plugin = AINewsletterEngine(api_key="TUA_OPENAI_KEY")
# newsletter = nl_plugin.create_newsletter("AI applicata al business", "imprenditori italiani")
