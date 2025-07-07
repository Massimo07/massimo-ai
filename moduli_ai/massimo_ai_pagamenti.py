import stripe
import json
import os

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY") or "INSERISCI-LA-TUA-KEY-QUI"
stripe.api_key = STRIPE_API_KEY

PLANS = {
    "monthly": 30000,   # in centesimi (€300)
    "annual": 350000,   # in centesimi (€3500)
}
MIN_PRICE = 30000

def crea_pagamento(user_email, referral_code=None, price=None, annual=False):
    amount = PLANS["annual"] if annual else PLANS["monthly"]
    price = price or amount
    if price < MIN_PRICE:
        raise Exception("Il prezzo non può essere inferiore al minimo!")
    description = "Abbonamento Massimo AI " + ("Annuale" if annual else "Mensile")
    metadata = {"referral": referral_code or "", "user_email": user_email}
    # Se il prezzo è maggiore del minimo, split automatico (Stripe Connect/Transfer)
    payment_intent = stripe.PaymentIntent.create(
        amount=price,
        currency='eur',
        description=description,
        receipt_email=user_email,
        metadata=metadata,
        # Qui puoi integrare split con Stripe Connect in automatico
    )
    return payment_intent.client_secret

def verifica_referral(referral_code):
    # Qui puoi leggere da un file referral.json o un DB chi è il partner
    # Esempio: ritorna dati del partner e quanto spetta come bonus
    try:
        with open("massimo_ai/referral.json", "r") as f:
            data = json.load(f)
        return data.get(referral_code)
    except:
        return None

def registra_pagamento(user_email, referral_code, price, annual):
    # Salva la transazione in un file pagamenti.json
    path = "massimo_ai/pagamenti.json"
    entry = {
        "user": user_email, "referral": referral_code, "price": price, "annual": annual
    }
    pagamenti = []
    if os.path.exists(path):
        with open(path, "r") as f:
            pagamenti = json.load(f)
    pagamenti.append(entry)
    with open(path, "w") as f:
        json.dump(pagamenti, f, indent=2, ensure_ascii=False)
    print("✅ Pagamento registrato")

if __name__ == "__main__":
    # Esempio demo (sostituisci con dati reali nei bot/app):
    email = input("Email utente: ")
    ref = input("Referral code (opzionale): ") or None
    price = int(input("Prezzo (centesimi, default=mensile): ") or 30000)
    annual = input("Annuale? (y/n): ").strip().lower() == "y"
    secret = crea_pagamento(email, ref, price, annual)
    print("Link pagamento:", secret)
    # Poi registra se necessario...
