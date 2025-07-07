# PAYMENTS MODULE – Massimo AI

Gestione completa e modulare di tutti i pagamenti:
- Stripe, PayPal, Webhook integrati
- Logging e explainability su ogni transazione/evento
- REST endpoint ready, integrabili nel main router

## Esempio REST
```bash
curl -X POST http://localhost:8000/payments/stripe -d '{"user_id":1,"amount":99}'
curl -X POST http://localhost:8000/payments/webhook -d '{"event":"payment_succeeded"}'
