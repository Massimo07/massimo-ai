"""
LOGGER – Logging avanzato Massimo AI.
- Multi-dest: console, file, cloud, Sentry, audit.
- Livelli, traceID, privacy, export.
"""
import logging
import sys

def get_logger(name: str, level: int = logging.INFO, file_path: str = None, cloud: bool = False):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    # Handler console
    if not logger.handlers:
        ch = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(name)s][%(process)d] %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    # Handler file
    if file_path and not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
        fh = logging.FileHandler(file_path)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(name)s][%(process)d] %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    # Handler cloud (esempio Sentry)
    if cloud:
        try:
            import sentry_sdk
            sentry_sdk.init(dsn=os.getenv("SENTRY_DSN"))
            # TODO: log Sentry come handler custom
        except ImportError:
            logger.warning("Sentry SDK non installato")
    return logger

# Uso esempio
logger = get_logger("massimoai", file_path="logs/app.log", cloud=False)
logger.info("Logger avviato e configurato.")
