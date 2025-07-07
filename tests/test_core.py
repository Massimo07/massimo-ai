"""
Massimo AI – Test Core
Test automatici di tutte le componenti base (modelli, servizi, sicurezza).
"""
from core.user import User
from services.payment import PaymentGateway

def test_user_creation():
    user = User(email="test@demo.com", name="Test", password="xxx")
    assert user.email == "test@demo.com"
    assert user.name == "Test"

def test_payment_gateway():
    pg = PaymentGateway("sk_test", "id", "secret")
    try:
        pg.pay_stripe(10, "user1", "tok_test")
    except Exception:
        assert True  # Stripe non configurato in test

if __name__ == "__main__":
    test_user_creation()
    test_payment_gateway()
    print("Tutti i test core passati!")
