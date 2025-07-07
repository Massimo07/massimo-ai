"""
Modulo: ai_lifebook_author.py
LifeBook AI: scrive, aggiorna, illustra il libro della vita di ogni membro. Storie, sogni, tappe, foto, obiettivi, ispirazione per generazioni future!
"""

LIFEBOOK = {}

def add_lifebook_page(user_id, page):
    LIFEBOOK.setdefault(user_id, []).append(page)
    return f"Nuova pagina aggiunta al LifeBook di {user_id}!"

def show_lifebook(user_id):
    pages = LIFEBOOK.get(user_id, [])
    return "\n".join(f"PAGINA: {p}" for p in pages) if pages else "LifeBook vuoto!"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    add_lifebook_page(1, "La mia prima iscrizione al Magic Team!")
    add_lifebook_page(1, "Ho raggiunto 30.000 PV — esperienza indimenticabile!")
    print(show_lifebook(1))
