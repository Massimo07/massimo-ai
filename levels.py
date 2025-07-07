"""
levels.py
Gestione avanzata dei livelli di Massimo AI e Live On Plus: regole di accesso, upgrade, badge, contenuti sbloccabili, prezzi, descrizioni e flow onboarding.
Pronto per gating contenuti, dashboard, CRM e automazioni Stripe.
"""

LEVELS = [
    {
        "id": 0,
        "key": "info_free",
        "name": "Info Free",
        "price": 0,
        "desc": "Accesso info aziendali, radio motivazionale 24/7, FAQ base e community.",
        "features": ["FAQ ufficiali", "Dettagli prodotti", "Piano Marketing step-by-step", "Follow-up iniziale", "Radio M AI 24/7", "news", "motivazione"]
    },
    {
        "id": 1,
        "key": "primo_passo",
        "name": "Primo Passo",
        "price": 15,
        "desc": "CRM base, FAQ avanzate, chatbot multicanale, primi step di formazione e materiali esclusivi.",
        "features": ["CRM contatti", "Template messaggi", "Quiz formativi", "Leaderboard base", "Supporto bot 24/7", "Tutorial onboarding", "quiz", "supporto dedicato"]
    },
    {
        "id": 2,
        "key": "cambio_vita",
        "name": "Cambio Vita",
        "price": 40,
        "desc": "Accesso a strategie di crescita, coaching, badge speciali.",
        "features": ["Coaching", "challenge", "gamification avanzata"]
    },
    {
        "id": 3,
        "key": "mentalita_vincente",
        "name": "Mentalità Vincente",
        "price": 70,
        "desc": "Formazione mindset, badge esclusivi, accesso contenuti premium.",
        "features": ["Masterclass", "formazione avanzata", "accesso contenuti top"]
    },
    {
        "id": 4,
        "key": "crescita_esponenziale",
        "name": "Crescita Esponenziale",
        "price": 110,
        "desc": "Percorsi di crescita accelerata, leaderboard premium.",
        "features": ["Percorsi personalizzati", "leaderboard avanzata"]
    },
    {
        "id": 5,
        "key": "imprenditore_libero",
        "name": "Imprenditore Libero",
        "price": 160,
        "desc": "Formazione imprenditoriale, supporto 1:1, mentoring.",
        "features": ["Mentoring", "dashboard imprenditori", "priority support"]
    },
    {
        "id": 6,
        "key": "guida_team",
        "name": "Guida del Team",
        "price": 220,
        "desc": "Gestione avanzata team, strumenti esclusivi, automazioni complete.",
        "features": ["Gestione team", "tool avanzati", "CRM premium"]
    },
    {
        "id": 7,
        "key": "network_leggendario",
        "name": "Network Leggendario",
        "price": 300,
        "desc": "Tutti i vantaggi, badge elite, eventi, contenuti e AI potenziata.",
        "features": ["AI avanzata", "eventi esclusivi", "tutti i badge", "upgrade istantaneo"]
    },
]

def get_level(key):
    return next((lvl for lvl in LEVELS if lvl.get("key") == key or lvl.get("id") == key), None)

def get_all_levels():
    return LEVELS

def next_level(current_key):
    keys = [lvl["key"] for lvl in LEVELS]
    if current_key in keys and keys.index(current_key) < len(keys) - 1:
        return LEVELS[keys.index(current_key) + 1]
    return None

def level_by_id(level_id):
    return next((lvl for lvl in LEVELS if lvl["id"] == level_id), None)

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(get_level("primo_passo"))
    print(next_level("primo_passo"))
    for lvl in get_all_levels():
        print(f"{lvl['id']} - {lvl['name']} — €{lvl['price']}")
