import os
import re

def patch_filters_py(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Sostituisci import
    content = re.sub(
        r"from telegram\.ext import Filters",
        "from telegram.ext import filters",
        content
    )

    # Sostituisci tutte le occorrenze di Filters.text, Filters.command ecc.
    content = re.sub(r"Filters\.text", "filters.TEXT", content)
    content = re.sub(r"Filters\.command", "filters.COMMAND", content)
    content = re.sub(r"Filters\.photo", "filters.PHOTO", content)
    content = re.sub(r"Filters\.video", "filters.VIDEO", content)
    content = re.sub(r"Filters\.audio", "filters.AUDIO", content)
    content = re.sub(r"Filters\.document", "filters.DOCUMENT", content)
    content = re.sub(r"Filters\.location", "filters.LOCATION", content)
    content = re.sub(r"Filters\.all", "filters.ALL", content)
    content = re.sub(r"Filters\.status_update", "filters.STATUS_UPDATE", content)
    content = re.sub(r"Filters\.update", "filters.UPDATE", content)
    content = re.sub(r"Filters\.user", "filters.USER", content)
    content = re.sub(r"Filters\.forwarded", "filters.FORWARDED", content)
    content = re.sub(r"Filters\.reply", "filters.REPLY", content)
    content = re.sub(r"Filters\.entity", "filters.ENTITY", content)
    content = re.sub(r"Filters\.voice", "filters.VOICE", content)
    content = re.sub(r"Filters\.animation", "filters.ANIMATION", content)
    content = re.sub(r"Filters\.sticker", "filters.STICKER", content)
    content = re.sub(r"Filters\.video_note", "filters.VIDEO_NOTE", content)
    content = re.sub(r"Filters\.contact", "filters.CONTACT", content)
    content = re.sub(r"Filters\.game", "filters.GAME", content)
    content = re.sub(r"Filters\.venue", "filters.VENUE", content)
    content = re.sub(r"Filters\.poll", "filters.POLL", content)
    content = re.sub(r"Filters\.passport_data", "filters.PASSPORT_DATA", content)

    # Salva solo se c'è una modifica
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def patch_all_py(rootdir):
    for dirpath, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(dirpath, file)
                try:
                    patch_filters_py(path)
                    print(f"✅ Patchato: {path}")
                except Exception as e:
                    print(f"⚠️  Errore su {path}: {e}")

if __name__ == "__main__":
    patch_all_py(".")
    print("🚀 Patch di massa sui Filters completata! Ora puoi lanciare il bot.")
