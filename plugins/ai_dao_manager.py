# /plugins_ai/ai_dao_manager.py

import openai

class AIDAOManager:
    def __init__(self, api_key):
        openai.api_key = api_key

    def create_dao(self, purpose, member_roles, voting_model, language="it"):
        prompt = (
            f"Progetta una DAO per: {purpose}, ruoli membri: {member_roles}, modello votazione: {voting_model}, lingua {language}. "
            "Suggerisci: struttura governance, incentivi token, onboarding, esempi di regole chiave."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# dao_plugin = AIDAOManager(api_key="TUA_OPENAI_KEY")
# dao_idea = dao_plugin.create_dao("Comunità di innovatori AI", "admin, membro, validatore", "1 persona 1 voto")
