import stripe
import os
import json

# Prendi la tua chiave segreta dalle variabili d'ambiente
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
if not stripe.api_key:
    raise Exception("Devi impostare STRIPE_SECRET_KEY nelle variabili d'ambiente")

# I livelli definiti con nome esatto e prezzo (in euro)
levels = [
    ("Info Free", 0),
    ("Primo Passo", 15),
    ("Cambio Vita", 40),
    ("Mentalità Vincente", 70),
    ("Crescita Esponenziale", 110),
    ("Imprenditore Libero", 160),
    ("Guida del Team", 220),
    ("Network Leggendario", 300)
]

created = []

for name, price in levels:
    # Crea il prodotto
    product = stripe.Product.create(
        name=f"Massimo AI – {name}",
        description=f"Abbonamento Massimo AI, livello {name}"
    )
    # Crea il prezzo di tipo Abbonamento mensile
    price_obj = stripe.Price.create(
        unit_amount=int(price * 100),  # centesimi
        currency="eur",
        recurring={"interval": "month"},
        product=product.id
    )
    created.append({
        "Livello": name,
        "Product ID": product.id,
        "Price ID": price_obj.id
    })

# Stampa a video il risultato
print(json.dumps(created, indent=2))
