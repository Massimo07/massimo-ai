"""
core/logging.py – Logging evoluto (file, console, rotating, alert founder).
"""

import logging
from logging.handlers import RotatingFileHandler

def setup_logging(logfile="massimoai.log"):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s – %(message)s")

    # Console
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File + rotazione
    fh = RotatingFileHandler(logfile, maxBytes=2*1024*1024, backupCount=3)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logging.info("[LOGGING] Logging inizializzato su console e file.")

setup_logging()
