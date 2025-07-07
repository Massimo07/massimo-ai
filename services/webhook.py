"""
WebhookService – Gestione webhook in/out, trigger automazioni, sicurezza firma.
"""

import logging
import hmac
import hashlib
from typing import Dict, Any

class WebhookError(Exception):
    pass

class WebhookService:
    SECRET = "CAMBIAQUESTO"

    def verify_signature(self, payload: bytes, signature: str) -> bool:
        mac = hmac.new(self.SECRET.encode(), payload, hashlib.sha256).hexdigest()
        return hmac.compare_digest(mac, signature)

    def handle_incoming(self, data: Dict[str, Any], signature: str) -> bool:
        if not self.verify_signature(str(data).encode(), signature):
            logging.warning(f"[WEBHOOK] Firma non valida!")
            raise WebhookError("Webhook firma non valida")
        logging.info(f"[WEBHOOK] Ricevuto evento: {data.get('event', 'unknown')}")
        # Qui lancia l'automazione vera (es: new payment, user created…)
        return True

    def emit(self, url: str, payload: Dict[str, Any]):
        # Placeholder: invio reale webhook (requests.post), con retry
        logging.info(f"[WEBHOOK] Emesso webhook a {url} payload={str(payload)[:80]}...")
        return True
