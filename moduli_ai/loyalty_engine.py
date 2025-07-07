"""
Modulo: loyalty_engine.py
Motore punti fedeltà: ogni azione del team/cliente genera punti, livelli, reward automatici, premi, cashback, VIP.
"""

LOYALTY = {}

def add_loyalty_points(user_id, action, points):
    user = LOYALTY.setdefault(user_id, {"total": 0, "history": []})
    user["total"] += points
    user["history"].append({"action": action, "points": points})
    return user["total"]

def get_loyalty_status(user_id):
    user = LOYALTY.get(user_id, {})
    total = user.get("total", 0)
    if total > 1000:
        return "VIP Gold"
    elif total > 500:
        return "VIP Silver"
    elif total > 100:
        return "Member"
    else:
        return "Starter"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(add_loyalty_points(1, "ordine", 50))
    print(add_loyalty_points(1, "referral", 200))
    print(get_loyalty_status(1))
