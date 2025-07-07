import stripe, os, json

# Usa la chiave LIVE nelle env vars
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
if not stripe.api_key:
    raise Exception("Devi impostare STRIPE_SECRET_KEY con la tua chiave LIVE")

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
    prod = stripe.Product.create(
        name=f"Massimo AI – {name}",
        description=name
    )
    price_obj = stripe.Price.create(
        unit_amount=price * 100,
        currency="eur",
        recurring={"interval": "month"},
        product=prod.id
    )
    session = stripe.checkout.Session.create(
        mode="subscription",
        line_items=[{"price": price_obj.id, "quantity": 1}],
        success_url="https://t.me/Massimo_AI_bot",
        cancel_url="https://t.me/Massimo_AI_bot"
    )
    created.append({
        "livello": name,
        "product_id": prod.id,
        "price_id": price_obj.id,
        "checkout_link": session.url
    })

print(json.dumps(created, indent=2, ensure_ascii=False))
