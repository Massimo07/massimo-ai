# /services/paypal_service.py

import paypalrestsdk
import os

# Configurazione con le credenziali PayPal dal tuo .env
paypalrestsdk.configure({
  "mode": os.getenv("PAYPAL_MODE", "sandbox"),  # "sandbox" o "live"
  "client_id": os.getenv("PAYPAL_CLIENT_ID"),
  "client_secret": os.getenv("PAYPAL_CLIENT_SECRET")
})

def create_payment(plan, success_url, cancel_url):
    """
    Crea una transazione PayPal per abbonamento o acquisto singolo.
    """
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": success_url,
            "cancel_url": cancel_url
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": plan["name"],
                    "sku": plan["id"],
                    "price": str(plan["price"]),
                    "currency": "EUR",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": str(plan["price"]),
                "currency": "EUR"
            },
            "description": f"Acquisto/abbonamento a {plan['name']}"
        }]
    })

    if payment.create():
        # Trova l’URL PayPal dove redirectare l’utente
        for link in payment.links:
            if link.method == "REDIRECT":
                return link.href
    else:
        raise Exception(payment.error)

def execute_payment(payment_id, payer_id):
    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({"payer_id": payer_id}):
        return True
    else:
        raise Exception(payment.error)
