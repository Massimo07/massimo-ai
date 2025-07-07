"""
FeedbackService – Raccolta, analisi e report feedback utenti (survey, NPS, A/B test).
Pronto per dashboard e analytics AI, sicurezza, logging avanzato.
"""

import logging
from datetime import datetime
from typing import List, Dict, Optional
from collections import Counter

class FeedbackError(Exception):
    pass

class FeedbackService:
    def __init__(self):
        self._feedbacks: List[Dict] = []

    def submit(self, user_id: str, text: str, category: str = "general", metadata: Optional[dict]=None) -> Dict:
        if not text or not user_id:
            raise FeedbackError("Testo e user_id sono obbligatori")
        entry = {
            "user_id": user_id,
            "text": text,
            "category": category,
            "date": datetime.utcnow().isoformat(),
            "metadata": metadata or {}
        }
        self._feedbacks.append(entry)
        logging.info(f"[FEEDBACK] {category} da {user_id}: '{text[:50]}...'")
        return entry

    def get_all(self, category: Optional[str]=None) -> List[Dict]:
        if category:
            return [f for f in self._feedbacks if f["category"] == category]
        return self._feedbacks

    def get_stats(self) -> Dict:
        categories = [f["category"] for f in self._feedbacks]
        return dict(Counter(categories))

    def purge(self, before: Optional[str]=None) -> int:
        """Elimina feedback più vecchi di una certa data (ISO8601)"""
        if before:
            before_dt = datetime.fromisoformat(before)
            old_count = len(self._feedbacks)
            self._feedbacks = [f for f in self._feedbacks if datetime.fromisoformat(f["date"]) > before_dt]
            logging.info(f"[FEEDBACK] Purge: rimossi {old_count - len(self._feedbacks)} feedback")
            return old_count - len(self._feedbacks)
        return 0
