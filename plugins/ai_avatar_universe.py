"""
Modulo: ai_avatar_universe.py
Ogni membro ha il proprio avatar AI: evoluzione, skills, badge, ranking, premi NFT/badge su blockchain. Ogni successo fa evolvere il tuo alter ego!
"""

import random

AVATARS = {}

def create_avatar(user_id, style="motivational"):
    avatar = {"level": 1, "skills": [], "badges": [], "style": style}
    AVATARS[user_id] = avatar
    return avatar

def evolve_avatar(user_id, skill):
    avatar = AVATARS.get(user_id)
    if not avatar:
        return "Nessun avatar trovato."
    avatar["skills"].append(skill)
    if len(avatar["skills"]) % 3 == 0:
        avatar["level"] += 1
        avatar["badges"].append(f"Badge livello {avatar['level']}")
    return avatar

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(create_avatar(1))
    print(evolve_avatar(1, "public speaking"))
    print(evolve_avatar(1, "recruitment"))
    print(evolve_avatar(1, "leadership"))
