"""
Modulo: knowledge_base.py
Knowledge base centralizzata per prodotti Live On Plus, piano marketing, FAQ, obiezioni e motivazione.
Espandibile da admin e pronta per prompt AI (moduli agents, openai_service).
"""

PRODUCTS = {
    "acido ialuronico": {
        "desc": "L’Acido Ialuronico Live On Plus idrata profondamente e dona elasticità alla pelle.",
        "tip": "Perfetto per chi vuole combattere rughe e segni del tempo.",
        "price": "€39"
    },
    "bava di lumaca": {
        "desc": "La bava di lumaca Live On Plus rigenera, illumina e cicatrizza.",
        "tip": "Ottima per pelli segnate o con imperfezioni.",
        "price": "€45"
    },
    "vitamina c": {
        "desc": "Vitamina C Live On Plus: antiossidante, illuminante, protegge dai radicali liberi.",
        "tip": "Ideale per chi vuole un incarnato più uniforme.",
        "price": "€29"
    }
    # Espandi con tutti i prodotti!
}

MARKETING = {
    "Customer": "Acquista i prodotti Live On Plus a prezzo scontato.",
    "Junior": "Accedi ai primi bonus e inizia a creare il tuo team.",
    "Visor": "Più bonus e formazione dedicata.",
    "Super Visor": "Guidi un team, accedi ai premi top.",
    "Ambassador": "Massima leadership, bonus esclusivi e viaggi premio."
}

FAQ = [
    {"q": "Come mi iscrivo?", "a": "Basta chiedere il link referral al tuo sponsor e compilare il modulo."},
    {"q": "Come faccio l’ordine?", "a": "Accedi al sito Live On Plus, scegli i prodotti e segui la procedura."},
    {"q": "Come guadagno?", "a": "Invita persone nel team e guadagni da ogni ordine loro e tuo!"},
]

OBJECTIONS = [
    {"q": "Non credo funzioni.", "a": "Ci sono centinaia di testimonianze e risultati nel Magic Team!"},
    {"q": "Non so vendere.", "a": "Nessuno nasce venditore: hai formazione e strumenti automatici che ti aiutano passo passo."},
    {"q": "Non ho tempo.", "a": "Anche solo 10 minuti al giorno bastano per far crescere il tuo business con Massimo AI!"},
]

MOTIVATION = [
    "Il successo è la somma di piccoli sforzi ripetuti ogni giorno.",
    "Non arrenderti: ogni leader era uno sconosciuto prima di crederci.",
    "Con Live On Plus e Massimo AI, non sei mai solo!"
]

# Utility per prompt AI
def get_product_info(name):
    return PRODUCTS.get(name.lower())

def get_marketing_info(level):
    return MARKETING.get(level, "Chiedi più dettagli al tuo sponsor o a Massimo AI!")

def get_faq(question):
    for faq in FAQ:
        if question.lower() in faq['q'].lower():
            return faq['a']
    return None

def get_objection_response(obj):
    for o in OBJECTIONS:
        if obj.lower() in o['q'].lower():
            return o['a']
    return None

def get_motivation():
    import random
    return random.choice(MOTIVATION)

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(get_product_info("bava di lumaca"))
    print(get_marketing_info("Ambassador"))
    print(get_faq("Come mi iscrivo?"))
    print(get_objection_response("Non ho tempo."))
    print(get_motivation())
