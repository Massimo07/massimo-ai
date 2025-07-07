import os
import stripe
from fastapi import APIRouter, HTTPException, Request
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
router = APIRouter()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_xxxxx")

# Modello livelli abbonamento (esempio)
LEVELS = {
    "start": {"price_id": "price_1...", "amount": 1500, "desc": "Start Level"},
    "gold":  {"price_id": "price_2...", "amount": 7000, "desc": "Gold Level"},
}

class StripeSessionRequest(BaseModel):
    level: str
    email: str

@router.post("/pagamento/crea-sessione", tags=["Stripe"])
def crea_sessione_pagamento(body: StripeSessionRequest):
    if body.level not in LEVELS:
        raise HTTPException(status_code=400, detail="Livello non valido")
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            customer_email=body.email,
            line_items=[{
                "price": LEVELS[body.level]["price_id"],
                "quantity": 1,
            }],
            mode="payment",
            success_url="http://localhost:8000/successo?session_id={CHECKOUT_SESSION_ID}",
            cancel_url="http://localhost:8000/annullato",
        )
        return {"checkout_url": session.url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/pagamento/webhook", tags=["Stripe"])
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')
    endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET", "")
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Webhook error: {e}")
    # Qui aggiorni lo stato nel DB/utente!
    return {"status": "received"}
