# /plugins_ai/ai_community_rewards.py

import openai

class AICommunityRewards:
    def __init__(self, api_key):
        openai.api_key = api_key

    def reward_system(self, context, actions, language="it"):
        prompt = (
            f"Crea un sistema di reward per {context}, azioni che generano punti: {actions}, lingua {language}. "
            "Suggerisci badge, livelli, premi, sistema ranking, esempi di premi speciali."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# rewards_plugin = AICommunityRewards(api_key="TUA_OPENAI_KEY")
# rewards = rewards_plugin.reward_system("forum Massimo AI", ["post utili", "aiuto a nuovi membri"])
