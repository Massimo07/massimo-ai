"""
Modulo: gamification_engine.py
Motore gamification: gestisce punti, challenge, badge, premi, leaderboard aggiornata in tempo reale. Aumenta engagement e retention!
"""

import datetime

USERS = {}
CHALLENGES = []
LEADERBOARD = []

def award_points(user_id, points, reason):
    user = USERS.setdefault(user_id, {"points": 0, "history": []})
    user["points"] += points
    user["history"].append({
        "date": datetime.datetime.now().isoformat(),
        "points": points,
        "reason": reason
    })
    update_leaderboard()
    return user["points"]

def create_challenge(title, reward, end_date):
    CHALLENGES.append({
        "title": title,
        "reward": reward,
        "end_date": end_date,
        "participants": []
    })

def participate(user_id, challenge_title):
    for ch in CHALLENGES:
        if ch["title"] == challenge_title:
            ch["participants"].append(user_id)
            return f"{user_id} iscritto alla sfida '{challenge_title}'!"
    return "Challenge non trovata!"

def update_leaderboard():
    global LEADERBOARD
    LEADERBOARD = sorted(USERS.items(), key=lambda x: x[1]["points"], reverse=True)

def get_leaderboard(top=10):
    return LEADERBOARD[:top]

# --- ESEMPIO USO ---
if __name__ == "__main__":
    award_points(1, 50, "Registrazione")
    award_points(2, 80, "Recruitment")
    create_challenge("Sfida Estate", "NFT Badge", "2025-08-01")
    participate(1, "Sfida Estate")
    update_leaderboard()
    print(get_leaderboard())
