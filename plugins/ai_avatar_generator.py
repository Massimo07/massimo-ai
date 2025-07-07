# /plugins_ai/ai_avatar_generator.py

import requests

class AIAvatarGenerator:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_avatar(self, prompt: str, size="512x512"):
        url = "https://api.openai.com/v1/images/generations"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": prompt + ", volto, sfondo neutro, per social",
            "n": 1,
            "size": size
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.ok:
            image_url = response.json()["data"][0]["url"]
            return image_url
        else:
            return {"error": response.text}

# USO:
# avatar_plugin = AIAvatarGenerator(api_key="TUA_OPENAI_KEY")
# url = avatar_plugin.generate_avatar("giovane imprenditore italiano, sorriso, look dinamico")
