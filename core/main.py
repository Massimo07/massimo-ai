"""
core/__main__.py – Avvio diretto core per debug/healthcheck
"""
from core.config import config
from core.logger import massimo_logger

if __name__ == "__main__":
    print(f"✅ Massimo AI Core loaded. Version: {config.version}")
    massimo_logger.info("Healthcheck core main OK")
