"""
Modulo: vision_board.py
Vision board digitale: ogni membro crea il suo collage di sogni/obiettivi/immagini motivazionali, aggiornabile e visibile da dashboard/bot/app.
"""

import json
import os

def create_vision_board(user_id, items):
    # items = [{"img": "https://...", "text": "Voglio una casa al mare!"}, ...]
    fname = f"vision_board_{user_id}.json"
    with open(fname, "w") as f:
        json.dump(items, f, indent=2)
    return fname

def get_vision_board(user_id):
    fname = f"vision_board_{user_id}.json"
    if os.path.exists(fname):
        with open(fname) as f:
            return json.load(f)
    return []

# --- ESEMPIO USO ---
if __name__ == "__main__":
    items = [
        {"img": "https://dummyimage.com/200x200/ffda00/000&text=Mare", "text": "Casa al mare"},
        {"img": "https://dummyimage.com/200x200/ffd700/001a3d&text=Auto", "text": "Auto nuova"},
        {"img": "https://dummyimage.com/200x200/00cfff/fff&text=Libertà", "text": "Libertà finanziaria"}
    ]
    print(create_vision_board(1, items))
    print(get_vision_board(1))
