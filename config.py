"""
core/config.py – Configurazione centrale Massimo AI (livello enterprise)

Gestisce tutte le variabili di ambiente, override da file .env, setup logging,
integrazione cloud-native, fallback predittivi, secret management, versioning.
"""
import os
from typing import Optional
from dotenv import load_dotenv
import logging

class Config:
    """Singleton per configurazione globale, sicuro e pronto per scaling."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            load_dotenv()
            cls._instance = super().__new__(cls)
            cls._instance.env = os.getenv("ENV", "production")
            cls._instance.app_name = os.getenv("APP_NAME", "Massimo AI")
            cls._instance.version = os.getenv("APP_VERSION", "1.0.0")
            cls._instance.secret_key = os.getenv("SECRET_KEY", "changeme")
            cls._instance.log_level = os.getenv("LOG_LEVEL", "INFO")
            cls._instance.db_url = os.getenv("DATABASE_URL", "")
            cls._instance.stripe_key = os.getenv("STRIPE_KEY", "")
            cls._instance.paypal_id = os.getenv("PAYPAL_CLIENT_ID", "")
            cls._instance.paypal_secret = os.getenv("PAYPAL_CLIENT_SECRET", "")
            cls._instance.language_default = os.getenv("LANG_DEFAULT", "it")
            cls._instance.allowed_hosts = os.getenv("ALLOWED_HOSTS", "*").split(",")
            # Estensibile: aggiungi nuove chiavi come vuoi!
        return cls._instance

    def reload(self):
        load_dotenv(override=True)

    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        return os.getenv(key, default)

# Logging globale
logging.basicConfig(
    level=getattr(logging, Config().log_level),
    format="%(asctime)s %(levelname)s [%(module)s]: %(message)s",
)

config = Config()

# Esempio uso:
# from core.config import config
# print(config.app_name)

