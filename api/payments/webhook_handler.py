# api/payments/webhook_handler.py
"""
PAYMENTS – WEBHOOK HANDLER (Massimo AI)
Gestione webhook di pagamenti (Stripe, PayPal), logging e audit.

- Endpoint: POST /payments/webhook
- Logging e explainability per ogni evento ricevuto
"""

from fastapi import APIRouter, Request
import logging

router = APIRouter()
logger = logging.getLogger("payments.webhook")
logger.setLevel(logging.INFO)

@router.post("/payments/webhook", tags=["payments-webhook"])
async def handle_payment_webhook(request: Request) -> dict:
    """
    Riceve ed elabora webhook di pagamento da Stripe/PayPal (audit, explain).
    """
    payload = await request.json()
    logger.info(f"[payments.webhook] Webhook ricevuto: {payload}")
    return {"status": "ok", "explain": "Webhook pagamento ricevuto e processato."}
