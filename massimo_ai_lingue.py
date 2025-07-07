import json

# Lista ISO 639-1 di tutte le lingue europee + russo + cinese + arabo
LINGUE = [
    "it", "en", "fr", "de", "es", "pt", "nl", "el", "pl", "cs", "sk", "ro",
    "bg", "hr", "hu", "sl", "et", "lv", "lt", "fi", "da", "sv", "no", "is",
    "tr", "mt", "ga", "ru", "zh", "ar"
]

DESCR = {
    "it": "Italiano", "en": "English", "fr": "Français", "de": "Deutsch", "es": "Español",
    "pt": "Português", "nl": "Nederlands", "el": "Ελληνικά", "pl": "Polski", "cs": "Čeština",
    "sk": "Slovenčina", "ro": "Română", "bg": "Български", "hr": "Hrvatski", "hu": "Magyar",
    "sl": "Slovenščina", "et": "Eesti", "lv": "Latviešu", "lt": "Lietuvių", "fi": "Suomi",
    "da": "Dansk", "sv": "Svenska", "no": "Norsk", "is": "Íslenska", "tr": "Türkçe", "mt": "Malti",
    "ga": "Gaeilge", "ru": "Русский", "zh": "中文", "ar": "العربية"
}

with open("massimo_ai/lingue.json", "w", encoding="utf-8") as f:
    json.dump({"lingue": LINGUE, "descr": DESCR}, f, ensure_ascii=False, indent=2)
print("✅ File lingue creato in massimo_ai/lingue.json")
