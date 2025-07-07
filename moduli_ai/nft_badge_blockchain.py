"""
Modulo: nft_badge_blockchain.py
Mint badge NFT su blockchain (Polygon testnet) — ogni badge diventa un NFT vero, pronto per wallet e marketplace.
Usa Moralis API (https://moralis.io/) o altro provider NFT.
"""

import requests
import datetime
import logging

logger = logging.getLogger("massimoai.nft_badge_blockchain")

MORALIS_API_KEY = "INSERISCI_LA_TUA_CHIAVE_API_MORALIS"
NFT_CONTRACT_ADDRESS = "INSERISCI_IL_TUO_CONTRACT_NFT"
WALLET_ADMIN = "TUO_WALLET_METAMASK_O_ALTRO"
MORALIS_URL = "https://deep-index.moralis.io/api/v2/nft/mint"

def mint_nft(user_wallet, badge_name, badge_desc, image_url):
    metadata = {
        "name": badge_name,
        "description": badge_desc,
        "image": image_url,
        "attributes": [
            {"trait_type": "Type", "value": "Massimo AI Badge"},
            {"trait_type": "Date", "value": datetime.datetime.now().isoformat()}
        ]
    }
    payload = {
        "chain": "mumbai",  # Polygon testnet
        "to_address": user_wallet,
        "contract_address": NFT_CONTRACT_ADDRESS,
        "metadata": metadata
    }
    headers = {
        "X-API-Key": MORALIS_API_KEY,
        "Content-Type": "application/json"
    }
    resp = requests.post(MORALIS_URL, json=payload, headers=headers)
    logger.info(f"Mint NFT resp: {resp.text}")
    if resp.status_code == 201 or resp.status_code == 200:
        result = resp.json()
        # Link NFT su explorer:
        nft_url = f"https://mumbai.polygonscan.com/token/{NFT_CONTRACT_ADDRESS}?a={result.get('token_id', '')}"
        return {"status": "ok", "nft_url": nft_url}
    else:
        return {"status": "error", "detail": resp.text}

# --- ESEMPIO USO ---
if __name__ == "__main__":
    # Inserisci qui i dati reali per la prova!
    wallet = "0x0000000000000000000000000000000000000000"  # Metti qui un wallet di test
    badge = mint_nft(
        wallet,
        "Black Diamond",
        "Raggiunto livello Black Diamond su Massimo AI!",
        "https://link-tuo-logo-o-badge.png"
    )
    print(badge)
