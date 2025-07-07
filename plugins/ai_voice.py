# ai_voice.py
"""
Voce AI Engine: genera risposte vocali, clona voci, crea file audio/podcast da testo.
Pronto per ElevenLabs, Play.ht, Google TTS e sistemi vocali avanzati.
"""

import openai
import requests

class AIVoiceEngine:
    def __init__(self, elevenlabs_key):
        self.elevenlabs_key = elevenlabs_key

    def generate_voice(self, text, voice="default", output_file="output.mp3", language="it"):
        # Esempio con ElevenLabs
        url = "https://api.elevenlabs.io/v1/text-to-speech"
        headers = {"xi-api-key": self.elevenlabs_key}
        data = {"voice": voice, "text": text, "output_format": "mp3", "language": language}
        response = requests.post(url, headers=headers, json=data)
        if response.ok:
            with open(output_file, "wb") as f:
                f.write(response.content)
            return output_file
        else:
            return response.text

    def clone_voice(self, audio_sample_path, text, voice_name="MassimoAI"):
        # Demo: richiede ElevenLabs Voice Cloning abilitato
        url = "https://api.elevenlabs.io/v1/voice/clone"
        files = {'audio': open(audio_sample_path, 'rb')}
        data = {'voice_name': voice_name, 'text': text}
        headers = {'xi-api-key': self.elevenlabs_key}
        response = requests.post(url, headers=headers, files=files, data=data)
        if response.ok:
            with open("voice_cloned.mp3", "wb") as f:
                f.write(response.content)
            return "voice_cloned.mp3"
        else:
            return response.text
