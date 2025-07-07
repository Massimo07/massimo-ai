# /services/stripe_service.py

import stripe
import os

# Configurazione: prendi la key dallo .env per sicurezza!
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_checkout_session(user_id, plan, success_url, cancel_url):
    """
    Crea una sessione Stripe Checkout per abbonamento (o acquisto one-shot)
    """
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "eur",
                "product_data": {"name": plan["name"]},
                "unit_amount": int(plan["price"] * 100),  # Euro -> centesimi
                "recurring": {"interval": plan["interval"]},  # es. "month"
            },
            "quantity": 1,
        }],
        mode="subscription",
        customer_email=plan.get("email"),  # O passala da user profile
        metadata={"user_id": user_id, "plan_id": plan["id"]},
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session.url  # Da usare per redirect

def handle_webhook(event, db):
    """
    Gestisce gli eventi webhook Stripe: attivazione abbonamento, pagamento, cancellazione, ecc.
    """
    event_type = event["type"]
    data = event["data"]["object"]

    if event_type == "checkout.session.completed":
        user_id = data["metadata"]["user_id"]
        plan_id = data["metadata"]["plan_id"]
        # Aggiorna DB: attiva abbonamento, invia mail, ecc.
        db["subscriptions"][user_id] = {"plan_id": plan_id, "status": "active"}
    elif event_type == "invoice.payment_failed":
        # Gestione fallimento pagamento
        pass
    elif event_type == "customer.subscription.deleted":
        # Gestione disdetta
        pass
    # ...altri eventi gestibili
