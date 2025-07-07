# massimo_ai_struttura.py
import os
import json

# Tutte le lingue richieste
LINGUE = [
    "it","en","fr","de","es","pt","nl","pl","cs","sk","ro","bg","hr","hu","el",
    "fi","sv","da","lt","lv","et","sl","ga","mt","ru","zh","ar"
]

# Tutti i livelli con nomi ufficiali
LIVELLI = [
    "Info Free", "Primo Passo", "Cambio Vita", "Mentalità Vincente", "Crescita Esponenziale",
    "Imprenditore Libero", "Guida del Team", "Network Leggendario", "Founder"
]

# Tutti i corsi richiesti
CORSI = [
    "ADOBE", "OFFICE", "AI ASSISTENT", "AI COPYWRITING", "COPYWRITING", "AI VIDEO", "VIDEO EDITING",
    "AUTOMATION", "AUTOSTIMA", "AUTOTRAINING", "AVATAR AI", "CANVA", "FUNNEL", "GAMIFICATION",
    "GOOGLE SUITE", "LEADERSHIP", "MENTALITÀ DA MILIONARIO", "NETWORK MARKETING", "NOTION",
    "PERSONAL BRAND", "PLUGIN AUTOMAZIONI", "PODCAST", "PODCAST RADIO", "PRESENTAZIONE AZIENDALE",
    "PRESENTAZIONE PIANO MARKETING", "PRESENTAZIONE PRODOTTI", "RECRUTING", "SOCIA ADV", "SOCIAL",
    "TIK TOK", "TIME MANAGEMENT", "VENDITA", "VIDEO EDITING", "VR TRAINING", "WEB MASTER",
    "WEB DESIGN", "WEBINAR", "YOUTUBE"
]

# Elenco servizi (sintetico, uno per livello — da completare a piacere)
SERVIZI_LIVELLI = {
    0: ["Presentazione aziendale", "Piano marketing", "Vantaggi Live On Plus", "Magic Team", "Cataloghi PDF", "Consiglio prodotto", "FAQ", "Parliamone", "Vendita", "Rete", "Autoconsumo", "Libro", "Testimonianze", "Sponsor", "Motivazione del giorno", "Radio M AI", "Cambia lingua", "Invita un amico", "Futuro livelli"],
    1: ["Onboarding AI", "Menu multicanale", "Gestione contatti", "Mini-corsi", "Presentazione prodotti", "Consiglio AI", "FAQ dinamiche", "Motivazione", "Supporto emotivo", "Gamification base", "Storytelling", "Download materiali", "Social invite"],
    2: ["Duplicazione onboarding", "Social automation", "Follow-up evoluto", "Gamification Pro", "Eventi AI", "Mentorship AI", "Testimonianze AI", "Gruppi auto-gestiti", "Statistiche team"],
    3: ["CRM predittivo", "Analytics avanzati", "Automazioni multi-step", "Branding Coach", "Podcast/Radio", "Marketplace risorse", "Pagamenti/abbonamenti", "Referral AI", "Dashboard duplicazione", "Skill assessment AI"],
    4: ["Automazione totale", "Plugin marketplace", "AR/VR Training", "Skill marketplace", "Eventi mondiali", "Pagamenti multilivello", "Predictive analytics", "NFT/certificati blockchain", "Gestione documenti smart"],
    5: ["Avatar AI personale", "Marketplace PRO", "Gestione multilivello internazionale", "Quantum Leap Simulator", "Reality Switcher", "Contratti smart", "Streaming TV", "Analytics predittiva", "NFT marketplace internazionale", "Report avanzati"],
    6: ["Superadmin", "Co-creazione moduli", "White-label", "Eventi VR globali", "Skill marketplace avanzato", "AI audit", "DAO governance", "Donazioni automatiche", "Formazione esportabile"],
    7: ["Tutto sbloccato", "AI generativa autonoma", "Digital Twin evolutivo", "Simulazione futuro", "Governance DAO totale", "Immortalità digitale", "AI collettiva", "Impatto sociale globale", "Tecnologie future", "Leadership mondiale"],
    8: ["Console Founder", "Override totale", "Cambia punto di vista", "Test/Dev riservato", "Gestione licenze", "Branding esclusivo", "Comunicazioni globali", "Roadmap personale", "Backup", "Gestione dati", "Espansione illimitata", "Override DAO", "Immortalità founder"]
}

def main():
    base_dir = "massimo_ai"
    os.makedirs(base_dir, exist_ok=True)
    # Crea struttura per livelli, corsi, lingue e servizi
    for i, livello in enumerate(LIVELLI):
        livello_dir = os.path.join(base_dir, f"livello_{i}_{livello.replace(' ', '_').lower()}")
        os.makedirs(livello_dir, exist_ok=True)
        for corso in CORSI:
            corso_dir = os.path.join(livello_dir, corso.replace(' ', '_').lower())
            os.makedirs(corso_dir, exist_ok=True)
            for lingua in LINGUE:
                lingua_dir = os.path.join(corso_dir, lingua)
                os.makedirs(lingua_dir, exist_ok=True)
        # Salva servizi in JSON
        servizi_file = os.path.join(livello_dir, f"servizi_{livello.replace(' ', '_').lower()}.json")
        with open(servizi_file, "w", encoding="utf-8") as f:
            json.dump(SERVIZI_LIVELLI.get(i, []), f, ensure_ascii=False, indent=2)
    print("✅ Struttura Massimo AI creata con livelli, corsi, lingue e servizi!")

if __name__ == "__main__":
    main()
