"""
Modulo: ai_network_museum.py
Network museum: ogni membro/evento/premio ha una “teca” virtuale, AI costruisce timeline, collezione oggetti digitali, video, podcast e storie.
"""

MUSEUM = {}

def add_museum_item(user_id, item, description):
    MUSEUM.setdefault(user_id, []).append({"item": item, "description": description})
    return f"Nuovo oggetto '{item}' aggiunto alla teca di {user_id}!"

def show_museum(user_id):
    items = MUSEUM.get(user_id, [])
    return "\n".join([f"{i['item']}: {i['description']}" for i in items]) if items else "Teca vuota!"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    add_museum_item(1, "Primo badge", "Il mio inizio con Magic Team")
    add_museum_item(1, "T-shirt evento", "Regalo all’evento internazionale 2025")
    print(show_museum(1))
