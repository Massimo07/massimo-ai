import os
import re
import subprocess
import sys

# Lista degli import standard da controllare e correggere
IMPORT_FIXES = [
    ("from telegram.ext import filters", "from telegram.ext import filters"),, ContextTypes
    ("from telegram.ext import ContextTypes", "from telegram.ext import ContextTypes"),, ContextTypes
    ("# from telegram.ext import Updater  # Obsoleto", "# # from telegram.ext import Updater  # Obsoleto  # Obsoleto"),, ContextTypes
    ("from telegram.ext import MessageHandler, filters", "from telegram.ext import MessageHandler, filters"),, ContextTypes
    ("from telegram.ext import ContextTypes", "from telegram.ext import ContextTypes"),, ContextTypes
    ("from telegram.ext import CommandHandler", "from telegram.ext import CommandHandler"),, ContextTypes
    ("from telegram.ext import ApplicationBuilder", "from telegram.ext import ApplicationBuilder"),, ContextTypes
    ("from telegram.ext import CallbackQueryHandler", "from telegram.ext import CallbackQueryHandler"),, ContextTypes
]

# Moduli e oggetti da importare se mancano
ENSURE_IMPORTS = [
    "from telegram.ext import ContextTypes",, ContextTypes
    "from telegram.ext import filters",, ContextTypes
]

def fix_imports_py(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    original = "".join(lines)
    changed = False

    # Applichiamo fix sulle stringhe
    for old, new in IMPORT_FIXES:
        original_new = original.replace(old, new)
        if original != original_new:
            print(f"🔧 Patch import: {old} → {new} in {filepath}")
            original = original_new
            changed = True

    # Verifica che gli ENSURE_IMPORTS siano presenti
    for imp in ENSURE_IMPORTS:
        if imp not in original:
            original = imp + "\n" + original
            print(f"➕ Aggiunto import: {imp} in {filepath}")
            changed = True

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(original)
    return changed

def scan_and_patch(directory):
    for root, dirs, files in os.walk(directory):
        # Non scansionare la cartella venv
        if "venv" in root:
            continue
        for file in files:
            if file.endswith(".py"):
                fix_imports_py(os.path.join(root, file))

def check_and_update_requirements():
    req_path = "requirements.txt"
    must_have = [
        "python-telegram-bot==22.1",
        "flask==3.0.3",
        "stripe==12.2.0",
        "openai==1.30.1",
        "apscheduler==3.10.4",
        "python-dotenv==1.0.1",
        "SQLAlchemy==2.0.30",
        "unittest2==1.1.0",
        "scikit-learn==1.4.2",
        "transformers==4.41.2",
        "requests==2.31.0",
        "beautifulsoup4==4.12.3",
        "selenium==4.21.0",
        "reportlab==4.1.0",
        "PyPDF2==3.0.1",
        "Pillow==10.3.0",
        "pandas==2.2.2",
        "numpy==1.26.4",
        "SpeechRecognition==3.10.1",
        "pyttsx3==2.90",
        "streamlit==1.35.0",
        "tqdm==4.66.4",
        "Werkzeug==3.0.3",
        "aiohttp==3.9.5",
        "qrcode==7.4.2",
        "webpush==1.0.2",
        "pytz==2024.1",
        "lxml==5.2.2"
    ]
    if not os.path.exists(req_path):
        print("📝 requirements.txt non trovato, lo creo!")
        with open(req_path, "w", encoding="utf-8") as f:
            for r in must_have:
                f.write(r + "\n")
    else:
        with open(req_path, "r", encoding="utf-8") as f:
            content = f.read()
        updated = False
        for r in must_have:
            if r not in content:
                print(f"🔧 Aggiorno requirements.txt con: {r}")
                content += r + "\n"
                updated = True
        if updated:
            with open(req_path, "w", encoding="utf-8") as f:
                f.write(content)

def auto_install_requirements():
    print("⏳ Installazione/aggiornamento pacchetti...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=False)
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=False)

if __name__ == "__main__":
    print("="*50)
    print("MASSIMO AI - MEGA PATCHER AUTOMATICO")
    print("="*50)
    scan_and_patch(".")
    check_and_update_requirements()
    auto_install_requirements()
    print("✅ Tutti i fix sono stati applicati!")
    print("🚀 Ora puoi lanciare main.py senza pensieri!")
    print("="*50)