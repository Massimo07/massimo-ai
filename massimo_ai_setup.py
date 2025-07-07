# massimo_ai_setup.py
import os
import json

# Nomi ufficiali dei livelli
LIVELLI = [
    "Info Free",  # Livello 0
    "Primo Passo",  # 1
    "Cambio Vita",  # 2
    "Mentalità Vincente",  # 3
    "Crescita Esponenziale",  # 4
    "Imprenditore Libero",  # 5
    "Guida del Team",  # 6
    "Network Leggendario",  # 7
    "Founder"  # 8 (SOLO TU)
]

# Menu servizi base come richiesto
SERVIZI_BASE = [
    "🏢 Presentazione aziendale",
    "💎 Presentazione piano marketing",
    "CHE VANTAGGI OFFRE LIVE ON PLUS",
    "🌟 Perché scegliere il Magic Team",
    "📚 Cataloghi prodotti",
    "🧴 Ti consiglio il prodotto adatto a te",
    "❓ Domande Frequenti (FAQ)",
    "🙋‍♂️ Hai bisogno di aiuto? PARLIAMONE",
    "🛒 Vuoi fare vendita?",
    "🌐 Vuoi fare rete?",
    "🏷 Vuoi fare autoconsumo?",
    "📖 Un libro per la tua crescita personale e professionale",
    "🔑 🏆 Testimonianze vere",
    "📞 Contatta il tuo sponsor",
    "🚀 Motivazione del giorno",
    "🎧 Radio M AI",
    "🔄 Cambia lingua",
    "🔗 Invita un amico",
    "E ORA… PREPARATI… SI ENTRA NEL FUTURO"
]

# Funzioni/servizi aggiuntivi (per ogni livello, in aggiunta ai servizi base)
LIVELLI_SERVIZI = {
    0: SERVIZI_BASE,
    1: SERVIZI_BASE + [
        "Onboarding AI motivazionale", "Microlearning", "Gamification base", "Storytelling personalizzato",
        "Download materiali essenziali", "Invita un amico (social invite)"
    ],
    2: SERVIZI_BASE + [
        "Duplicazione onboarding", "Social automation base", "Follow-up evoluto e reminder multicanale",
        "Gamification Pro", "Eventi AI base", "Mentorship AI base", "Testimonianze AI", "Gruppi auto-gestiti", "Statistiche team base"
    ],
    3: SERVIZI_BASE + [
        "CRM predittivo", "Analytics avanzati", "Automazioni multi-step", "Branding Coach AI",
        "Podcast/Radio AI", "Marketplace risorse", "Gestione abbonamenti", "Referral AI avanzato",
        "Dashboard engagement", "Skill assessment AI"
    ],
    4: SERVIZI_BASE + [
        "Automazione totale", "Plugin marketplace", "AR/VR Training", "Skill marketplace", "Gestione eventi mondiali",
        "Pagamenti multilivello", "Predictive analytics", "NFT/certificati blockchain", "Gestione documenti smart"
    ],
    5: SERVIZI_BASE + [
        "Avatar AI personale", "Marketplace PRO", "Gestione multilivello internazionale", "Quantum Leap Simulator",
        "Reality Switcher", "Gestione documenti e contratti smart", "Streaming TV personale", "Analytics predittiva totale",
        "Skill & NFT marketplace internazionale", "Gestione avanzata team cross-country"
    ],
    6: SERVIZI_BASE + [
        "Superadmin", "Co-creazione plug-in live", "Gestione white-label", "Eventi VR globali",
        "Skill marketplace avanzato", "AI audit & compliance", "DAO governance", "Donazioni automatiche", "Formazione esportabile"
    ],
    7: SERVIZI_BASE + [
        "AI generativa autonoma", "Digital Twin evolutivo", "Simulazione del futuro", "Governance DAO totale",
        "Immortalità digitale", "AI collettiva di team", "Impatto sociale globale", "Accesso a tecnologie future",
        "Leadership mondiale"
    ],
    8: SERVIZI_BASE + [
        "Console Founder", "Override totale", "Cambia punto di vista", "Test/Dev riservato", "Gestione licenze",
        "Branding esclusivo", "Comunicazioni globali", "Roadmap e release personale", "Backup/restore", "Supervisione dati/API/GDPR",
        "Espansione senza limiti", "Override DAO", "Immortalità founder"
    ]
}

# Genera struttura cartelle/servizi
def crea_struttura_massimo_ai():
    os.makedirs("massimo_ai", exist_ok=True)
    for idx, livello in enumerate(LIVELLI):
        folder = f"massimo_ai/livello_{idx}_{livello.replace(' ', '_').lower()}"
        os.makedirs(folder, exist_ok=True)
        servizi = LIVELLI_SERVIZI.get(idx, [])
        with open(f"{folder}/servizi_{livello.replace(' ', '_').lower()}.json", "w", encoding="utf-8") as f:
            json.dump(servizi, f, ensure_ascii=False, indent=2)
        print(f"✔️ Cartella e servizi per '{livello}' creata in {folder}")

    print("\n✅ STRUTTURA MASSIMO AI CREATA. TUTTI I LIVELLI PRONTI.\n")
    print("Ora puoi collegare ogni script specialistico su questa base (corsi, admin, bot, scraping, ecc).")

if __name__ == "__main__":
    crea_struttura_massimo_ai()
