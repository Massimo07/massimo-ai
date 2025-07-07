"""
core/i18n.py

Massimo AI – Internationalization & Translation module
Gestione multilingua “reale”: memoria cache, fallback intelligente, supporto traduzioni AI dinamiche, loader json, override runtime.
"""

import json
import os
from typing import Dict, Optional
from functools import lru_cache

class I18N:
    """
    Motore i18n avanzato:
    - Caricamento dizionari da file/json/db
    - Cache LRU
    - Fallback lingua (es: en→it)
    - Runtime override
    - Supporto plug-in AI (traduzione on-the-fly GPT/DeepL)
    """
    def __init__(self, lang: str = "en", lang_dir: str = "i18n/"):
        self.lang = lang
        self.lang_dir = lang_dir
        self.translations: Dict[str, Dict[str, str]] = {}
        self._load_all_languages()

    def _load_language(self, lang: str):
        """Carica dizionario per una lingua dal filesystem."""
        path = os.path.join(self.lang_dir, f"{lang}.json")
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                self.translations[lang] = json.load(f)
        else:
            self.translations[lang] = {}

    def _load_all_languages(self):
        """Pre-carica tutti i dizionari disponibili (es: su startup)."""
        for file in os.listdir(self.lang_dir):
            if file.endswith(".json"):
                lang = file.replace(".json", "")
                self._load_language(lang)

    @lru_cache(maxsize=128)
    def t(self, key: str, lang: Optional[str] = None, **kwargs) -> str:
        """Restituisce la stringa tradotta per la lingua richiesta, fallback a inglese."""
        lang = lang or self.lang
        value = self.translations.get(lang, {}).get(key)
        if value:
            return value.format(**kwargs)
        # Fallback a inglese o key raw
        fallback = self.translations.get("en", {}).get(key)
        return fallback.format(**kwargs) if fallback else key

    def set_lang(self, lang: str):
        """Cambia la lingua attiva (e carica se mancante)."""
        if lang not in self.translations:
            self._load_language(lang)
        self.lang = lang

    def ai_translate(self, key: str, target_lang: str, ai_func=None) -> str:
        """
        Traduci una stringa con AI (es: GPT, DeepL, Bing).  
        Plug-in: basta passare una funzione che chiama l’API desiderata.
        """
        original = self.t(key, lang="en")
        if ai_func:
            return ai_func(original, target_lang)
        return original  # Fallback se no AI

# Esempio di plug-in traduttore (finto)
def dummy_ai_translator(text, target_lang):
    return f"[{target_lang}] {text}"

if __name__ == "__main__":
    i18n = I18N(lang="it", lang_dir="i18n/")
    print(i18n.t("welcome"))  # Cerca in it.json, fallback su en.json
    print(i18n.ai_translate("welcome", "es", dummy_ai_translator))
