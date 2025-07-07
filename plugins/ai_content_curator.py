"""
Modulo: ai_content_curator.py
AI curator: trova, filtra, suggerisce contenuti top (post, articoli, news, video, podcast) per ispirare/formare il team.
"""

import random

CONTENT_DB = [
    {"type": "video", "title": "Leadership vincente", "url": "https://youtube.com/..."},
    {"type": "post", "title": "10 consigli per il successo", "url": "https://blog.com/..."},
    {"type": "podcast", "title": "Mentalità vincente", "url": "https://spotify.com/..."}
]

def suggest_content(topic="motivazione"):
    # In reale: scraping, AI ranking, filtri personalizzati
    return random.choice(CONTENT_DB)

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(suggest_content("successo"))
