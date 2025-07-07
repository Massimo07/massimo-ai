# /plugins_ai/ai_global_news_curator.py

import openai

class AIGlobalNewsCurator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def curate_news(self, topic, n_news=5, language="it"):
        prompt = (
            f"Cura e riassumi le {n_news} notizie più rilevanti al mondo su '{topic}', in lingua {language}. "
            "Per ogni news: fonte, sintesi, possibile impatto, suggerimento AI per business o crescita personale."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# news_plugin = AIGlobalNewsCurator(api_key="TUA_OPENAI_KEY")
# notizie = news_plugin.curate_news("Intelligenza artificiale")
