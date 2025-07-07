# /services/badge.py
BADGE_TYPES = {
    "Founder": {"icon": "👑", "color": "#FFD85C"},
    "Innovator": {"icon": "🚀", "color": "#8B5CFF"},
    "Beta Tester": {"icon": "🧪", "color": "#4EC9FF"},
    "Community Hero": {"icon": "🤝", "color": "#FF8F00"},
}

def assign_badge(user_id, badge_type, db):
    badge = BADGE_TYPES.get(badge_type)
    if not badge:
        raise ValueError("Badge non esistente")
    db["users"][user_id]["badges"].append(badge_type)
    return badge

def list_badges(user_id, db):
    return db["users"][user_id].get("badges", [])
