"""
Modulo: challenge_engine.py
Motore per creare, lanciare, tracciare e premiare challenge individuali o team: punti, premi, leaderboard, report, alert.
"""

import datetime

CHALLENGES = []

def create_challenge(title, desc, start, end, reward):
    ch = {
        "title": title,
        "desc": desc,
        "start": start,
        "end": end,
        "reward": reward,
        "participants": []
    }
    CHALLENGES.append(ch)
    return ch

def join_challenge(user_id, challenge_title):
    for ch in CHALLENGES:
        if ch["title"] == challenge_title:
            ch["participants"].append({"user_id": user_id, "joined": datetime.datetime.now().isoformat()})
            return "Iscrizione challenge OK"
    return "Challenge non trovata"

def report_challenge(challenge_title):
    for ch in CHALLENGES:
        if ch["title"] == challenge_title:
            return {
                "partecipanti": len(ch["participants"]),
                "premio": ch["reward"]
            }
    return {}

# --- ESEMPIO USO ---
if __name__ == "__main__":
    create_challenge("Sfida Black Diamond", "Raggiungi 30.000PV", "2025-07-01", "2025-07-31", "NFT Black Diamond")
    join_challenge(1, "Sfida Black Diamond")
    print(report_challenge("Sfida Black Diamond"))
