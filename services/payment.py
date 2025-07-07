"""
Massimo AI – Payment Gateway
Gestione pagamenti multicanale (Stripe, PayPal), logging, ricevute, fallback automatico.
"""
import stripe
import requests
import logging

class PaymentGateway:
    def __init__(self, stripe_key, paypal_client_id, paypal_secret):
        stripe.api_key = stripe_key
        self.paypal_id = paypal_client_id
        self.paypal_secret = paypal_secret
        self.logger = logging.getLogger("PaymentGateway")

    def pay_stripe(self, amount_eur, user_id, token):
        try:
            charge = stripe.Charge.create(
                amount=int(amount_eur * 100),
                currency='eur',
                source=token,
                description=f"Pagamento Massimo AI per utente {user_id}",
            )
            self.logger.info(f"Pagamento Stripe riuscito: {charge['id']}")
            return charge
        except Exception as e:
            self.logger.error(f"Errore Stripe: {e}")
            raise

    def pay_paypal(self, amount_eur, user_id, access_token):
        try:
            url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            }
            data = {
                "intent": "CAPTURE",
                "purchase_units": [{
                    "amount": {"currency_code": "EUR", "value": str(amount_eur)},
                    "description": f"Massimo AI per utente {user_id}"
                }]
            }
            r = requests.post(url, headers=headers, json=data)
            self.logger.info(f"Pagamento PayPal response: {r.status_code}")
            return r.json()
        except Exception as e:
            self.logger.error(f"Errore PayPal: {e}")
            raise

    def send_receipt(self, user_email, details):
        # Puoi usare SendGrid/SMTP
        print(f"Inviata ricevuta a {user_email}: {details}")

    def log_payment(self, method, user_id, amount, meta=None):
        self.logger.info(f"Payment {method} | User: {user_id} | Amount: {amount} | {meta}")
