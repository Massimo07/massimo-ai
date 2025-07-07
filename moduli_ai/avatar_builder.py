"""
Modulo: avatar_builder.py
Genera avatar AI custom: stile cartoon, professionale, motivazionale, per onboarding, team, NFT, badge, onboarding visivo.
"""

import random

def create_avatar(user_name, style="cartoon"):
    # Demo: in reale integri DALL-E, Stable Diffusion, AvatarAI, Fotor, ecc.
    styles = {
        "cartoon": "Cartoon colorato",
        "pro": "Look professionale, elegante",
        "motiv": "Stile motivazionale, colori oro/blu"
    }
    avatar_desc = f"Avatar per {user_name}, stile: {styles.get(style, 'originale')}"
    img_url = f"https://dummyimage.com/256x256/ffd700/001a3d&text={user_name[0]}"
    return {"desc": avatar_desc, "img": img_url}

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(create_avatar("Sara", style="motiv"))
