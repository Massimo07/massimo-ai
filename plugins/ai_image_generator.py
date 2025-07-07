# /plugins_ai/ai_image_generator.py

import requests

class AIImageGenerator:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_image(self, prompt: str, size="1024x1024"):
        url = "https://api.openai.com/v1/images/generations"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": prompt,
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
# img_plugin = AIImageGenerator(api_key="TUA_OPENAI_KEY")
# url = img_plugin.generate_image("un robot felice che programma in Python")
