# /plugins_ai/ai_chatbot_custom.py

import openai

class AICustomChatbot:
    def __init__(self, api_key, system_prompt=""):
        openai.api_key = api_key
        self.system_prompt = system_prompt

    def chat(self, user_message):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages
        )
        return response.choices[0].message.content

# USO:
# custom_bot = AICustomChatbot(api_key="TUA_OPENAI_KEY", system_prompt="Sei il coach motivazionale di Massimo AI.")
# risposta = custom_bot.chat("Come posso superare le mie paure?")
