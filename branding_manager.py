"""
Modulo: branding_manager.py
Gestione dinamica branding: puoi cambiare logo, claim, colori, immagini motivazionali da file/config o dashboard.
Perfetto per rebranding o evoluzione del team!
"""

import os
import json

BRANDING_PATH = "branding.json"

def load_branding():
    if not os.path.exists(BRANDING_PATH):
        branding = {
            "logo_url": "https://magicteam.it/logo.png",
            "primary_color": "#FFD700",
            "secondary_color": "#262626",
            "claim": "Sblocca il tuo potenziale con Massimo AI!",
            "motivation_images": []
        }
        with open(BRANDING_PATH, "w") as f:
            json.dump(branding, f, indent=2)
    with open(BRANDING_PATH) as f:
        return json.load(f)

def update_branding(new_data):
    branding = load_branding()
    branding.update(new_data)
    with open(BRANDING_PATH, "w") as f:
        json.dump(branding, f, indent=2)

if __name__ == "__main__":
    update_branding({"claim": "Vinci ogni giorno col Magic Team!"})
    print(load_branding())
