"""
Modulo: referral_magic.py
Gestione referral-link, tracciamento, monitoraggio conversioni, report, reward, scelta sponsor via dashboard/bot.
"""

import random
import string

REF_LINKS = {}

def generate_referral_link(user_id):
    ref_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    link = f"https://magicteam.live/signup?ref={ref_code}"
    REF_LINKS[user_id] = link
    return link

def get_referrer(user_id):
    return REF_LINKS.get(user_id, "Nessun referral registrato")

def report_referrals():
    return {uid: link for uid, link in REF_LINKS.items()}

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(generate_referral_link(1))
    print(report_referrals())
