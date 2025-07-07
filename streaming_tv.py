"""
Modulo: streaming_tv.py
Crea e gestisce una "web TV" interna: playlist video motivazionali, training, replay, dirette. Accesso per livelli e ruoli!
"""

VIDEOS = []

def add_video(title, url, level="Tutti"):
    VIDEOS.append({"title": title, "url": url, "level": level})
    return VIDEOS

def get_videos(level="Tutti"):
    # Solo i video per il livello dell’utente
    return [v for v in VIDEOS if v["level"] == level or v["level"] == "Tutti"]

# --- ESEMPIO USO ---
if __name__ == "__main__":
    add_video("Benvenuto in Massimo AI", "https://www.youtube.com/embed/dQw4w9WgXcQ", "Starter")
    add_video("Leadership Diamond", "https://www.youtube.com/embed/abc123", "Black Diamond")
    print(get_videos("Black Diamond"))
