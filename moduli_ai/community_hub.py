"""
Modulo: community_hub.py
Hub social/chat/eventi Magic Team: ogni utente può postare, commentare, partecipare a eventi, ricevere risposte AI e notifiche in tempo reale.
"""

import datetime
import logging

logger = logging.getLogger("massimoai.community_hub")

POSTS = []
EVENTS = []

def post_message(user_id, text):
    POSTS.append({
        "timestamp": datetime.datetime.now().isoformat(),
        "user_id": user_id,
        "text": text
    })
    logger.info(f"Nuovo post da {user_id}: {text}")

def get_feed(limit=20):
    return POSTS[-limit:]

def add_event(title, when, desc, link=""):
    EVENTS.append({
        "title": title,
