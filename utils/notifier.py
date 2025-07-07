"""
utils/notifier.py

Helper per notifiche rapide (log, email, Slack, SMS, ecc).
"""
import logging

def notify_log(message: str, level: str = "info"):
    getattr(logging, level, "info")(message)
