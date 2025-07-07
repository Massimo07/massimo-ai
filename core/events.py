"""
EVENTS – Event bus, hook asincroni, replay, log.
"""
from typing import Callable, Dict, List
import logging

class EventBus:
    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = {}

    def subscribe(self, event: str, handler: Callable):
        self._listeners.setdefault(event, []).append(handler)

    def publish(self, event: str, *args, **kwargs):
        handlers = self._listeners.get(event, [])
        for h in handlers:
            try:
                h(*args, **kwargs)
            except Exception as e:
                logging.error(f"[EventBus] Errore handler '{h}': {e}")

event_bus = EventBus()
