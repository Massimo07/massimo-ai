# /plugins_ai/ai_voiceover_generator.py

import requests

class AIVoiceOverGenerator:
    def __init__(self, elevenlabs_key, voice_id="EXAVITQu4vr4xnSDxMaL"):
        self.api_key = elevenlabs_key
        self.voice_id = voice_id

    def generate_voice(self, text: str, output_path="output_voice.mp3"):
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"
        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        data = {
            "text": text,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.7}
        }
        response = requests.post(url, headers=headers, json=data)
        if response.ok:
            with open(output_path, "wb") as f:
                f.write(response.content)
            return output_path
        else:
            return {"error": response.text}

# USO:
# voice_plugin = AIVoiceOverGenerator(elevenlabs_key="TUA_ELEVENLABS_KEY")
# path = voice_plugin.generate_voice("Benvenuto in Massimo AI!")
