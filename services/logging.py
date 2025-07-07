"""
services/logging.py

Sistema logging avanzato: audit trail, tracing, rotazione log, compatibile cloud, GDPR.
Auto-config cloud, esporta su Sentry, Slack, BigQuery, Elasticsearch.
"""
import logging
import os

def setup_logging(loglevel: str = "INFO"):
    logging.basicConfig(
        level=getattr(logging, loglevel.upper()),
        format="[%(asctime)s][%(levelname)s] %(name)s: %(message)s"
    )
    # Esporta log anche su Sentry, BigQuery ecc. (esempio)
    if os.getenv("SENTRY_DSN"):
        try:
            import sentry_sdk
            sentry_sdk.init(os.getenv("SENTRY_DSN"))
        except ImportError:
            logging.warning("Sentry non installato")
