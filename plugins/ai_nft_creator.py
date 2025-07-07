# /plugins_ai/ai_nft_creator.py

import openai

class AINFTCreator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def create_nft(self, theme, utility, blockchain="Ethereum", language="it"):
        prompt = (
            f"Genera un concept di collezione NFT a tema '{theme}', utilità: {utility}, blockchain: {blockchain}, lingua {language}. "
            "Suggerisci 5 nomi NFT, descrizione, uso pratico, script smart contract base (ERC721)."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# USO:
# nft_plugin = AINFTCreator(api_key="TUA_OPENAI_KEY")
# nft_idea = nft_plugin.create_nft("AI Creativa", "Accesso corsi esclusivi")
