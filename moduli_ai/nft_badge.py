"""
Modulo: nft_badge.py
Gestione badge e premi digitali come NFT: badge collezionabili, token unici per milestone, leadership e premi.
Pronto per blockchain (demo), premi custom, trading badge.
"""

import datetime
import logging

logger = logging.getLogger("massimoai.nft_badge")

BADGES = []

def mint_badge(user_id, badge_name, reason):
    badge = {
        "user_id": user_id,
        "badge_name": badge_name,
        "reason": reason,
        "timestamp": datetime.datetime.now().isoformat(),
        "nft_token": f"TOKEN_{user_id}_{badge_name}_{int(datetime.datetime.now().timestamp())}"
    }
    BADGES.append(badge)
    logger.info(f"Badge NFT mintato: {badge}")
    return badge

def list_badges(user_id=None):
    if user_id:
        return [b for b in BADGES if b["user_id"] == user_id]
    return BADGES

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(mint_badge(1, "Black Diamond", "Leadership straordinaria"))
    print(list_badges(1))
