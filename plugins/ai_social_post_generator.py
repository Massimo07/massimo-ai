# /plugins_ai/ai_social_post_generator.py

import openai

class AISocialPostGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_post(self, topic, tone="ispirazionale", platform="LinkedIn", language="it"):
        prompt = (
            f"Scrivi un post virale per {platform} su '{topic}', tono {tone}, in lingua {language}. "
            "Aggiungi 3 hashtag potenti e una call-to-action."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# post_plugin = AISocialPostGenerator(api_key="TUA_OPENAI_KEY")
# post = post_plugin.generate_post("Massimo AI rivoluziona il mondo", "ispirazionale", "LinkedIn", "it")
