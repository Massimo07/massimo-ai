import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    STRIPE_KEY = os.getenv("STRIPE_SECRET_KEY")
    OPENAI_KEY = os.getenv("OPENAI_KEY")
    # ...altri parametri se vuoi

settings = Settings()
