import os
import stripe
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

LEVEL_PRICES = {
    1: "price_1RXqw2GsG0e6XSfX5pBwxaQZ",
    2: "price_1RXqw4GsG0e6XSfXYLFsDFmI",
    3: "price_1RXqw5GsG0e6XSfX988zLPiB",
    4: "price_1RXqw6GsG0e6XSfXrVHQl676",
    5: "price_1RXqw7GsG0e6XSfXAtmAqUye",
    6: "price_1RXqw8GsG0e6XSfXJGI3GIkp",
    7: "price_1RXqwAGsG0e6XSfXOYofiQ6K",
}

def create_checkout_session(user_id: int, level: int, success_url: str, cancel_url: str) -> str:
    price_id = LEVEL_PRICES.get(level)
    if not price_id:
        raise ValueError("Livello non valido")

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        mode='subscription',
        line_items=[{'price': price_id, 'quantity': 1}],
        metadata={"user_id": str(user_id), "level": str(level)},
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session.url
