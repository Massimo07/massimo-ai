"""
Modulo: smart_reward.py
Premiazione automatica: badge, punti, gift, sconti, NFT, premi fisici… su base regole, challenge, milestones. Gestione e redemption centralizzata!
"""

REWARDS = []

def add_reward(user_id, reward_type, description):
    reward = {"user_id": user_id, "type": reward_type, "desc": description}
    REWARDS.append(reward)
    return reward

def get_rewards(user_id):
    return [r for r in REWARDS if r["user_id"] == user_id]

def redeem_reward(user_id, reward_type):
    for r in REWARDS:
        if r["user_id"] == user_id and r["type"] == reward_type:
            REWARDS.remove(r)
            return f"Reward {reward_type} per {user_id} riscattato!"
    return "Nessun reward da riscattare"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    add_reward(1, "Gift Card", "Buono Amazon 50€")
    add_reward(1, "NFT", "NFT Black Diamond")
    print(get_rewards(1))
    print(redeem_reward(1, "Gift Card"))
