# /plugins_ai/ai_video_script_generator.py

import openai

class AIVideoScriptGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_script(self, topic: str, style="ispirazionale"):
        prompt = (
            f"Scrivi uno script breve per un video su '{topic}' in stile {style}. "
            "Massimo impatto, apertura forte, chiusura memorabile."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        script = response.choices[0].message.content
        return script

# USO:
# video_plugin = AIVideoScriptGenerator(api_key="TUA_OPENAI_KEY")
# script = video_plugin.generate_script("come l'AI sta cambiando il mondo")
