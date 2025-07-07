from telegram.ext import CommandHandler
import os
import shutil
import glob
import subprocess
import sys
import re
import time

BACKUP_DIR = "backup_massimoai"
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Backup automatico dei file chiave
def backup_files():
    if not os.path.exists(os.path.join(SRC_DIR, BACKUP_DIR)):
        os.makedirs(os.path.join(SRC_DIR, BACKUP_DIR))
    for ext in ("*.py", ".env"):
        for f in glob.glob(os.path.join(SRC_DIR, ext)):
            shutil.copy(f, os.path.join(SRC_DIR, BACKUP_DIR, os.path.basename(f)))
    for root, dirs, files in os.walk(SRC_DIR):
        for f in files:
            if f.endswith(".py"):
                fullpath = os.path.join(root, f)
                shutil.copy(fullpath, os.path.join(SRC_DIR, BACKUP_DIR, f"sub_{f}"))

# 2. Correzione imports e sintassi telegram
def fix_imports_py(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()
    orig_code = code

    # Correggi import vecchi/nuovi per telegram.ext
    code = re.sub(r'from telegram\.ext import Filters', 'from telegram.ext import filters', code)
    code = re.sub(r'from telegram\.ext import\s*\((.*?)\)', lambda m: 'from telegram.ext import ' + ', '.join([x.strip() for x in m.group(1).replace('\n','').split(',') if x.strip()]), code, flags=re.DOTALL)
    # Correggi filtri errati nelle versioni più recenti
    code = re.sub(r'Filters\.', 'filters.', code)
    # Uniforma ContextTypes se serve
    code = code.replace('ContextTypes.DEFAULT_TYPE', 'ContextTypes.DEFAULT_TYPE')

    # Togli parentesi inutili in import
    code = re.sub(r'from telegram.ext import \((.*)\)', lambda m: f"from telegram.ext import {m.group(1).replace(',', ', ')}", code)

    # Rimuovi doppie virgole o virgole finali in import
    code = re.sub(r',\s*\)', ')', code)

    # Fix per import duplicati o sporchi
    code = re.sub(r'from telegram.ext import |+', 'from telegram.ext import ', code)
    code = re.sub(r'import \)', '', code)

    # Rimuovi eventuali linee vuote multiple
    code = re.sub(r'\n\n+', '\n\n', code)

    # Sistemazione indentazione minima
    lines = []
    for line in code.splitlines():
        lines.append(line.rstrip())
    code = "\n".join(lines)

    if code != orig_code:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"[PATCH] Corretto: {filepath}")

# 3. Fix variabili ambiente
def fix_env():
    env_file = os.path.join(SRC_DIR, ".env")
    if os.path.exists(env_file):
        with open(env_file, "r", encoding="utf-8") as f:
            env = f.read()
        orig_env = env
        env = re.sub(r"STRIPE_KEY=", "STRIPE_SECRET_KEY=", env)
        env = re.sub(r"STRIPE_PUBKEY=", "STRIPE_PUB_KEY=", env)
        # Add checks for missing
        if "STRIPE_SECRET_KEY" not in env:
            env += "\nSTRIPE_SECRET_KEY=sk_live_\n"
        if "STRIPE_PUB_KEY" not in env:
            env += "\nSTRIPE_PUB_KEY=pk_live_\n"
        if env != orig_env:
            with open(env_file, "w", encoding="utf-8") as f:
                f.write(env)
            print("[PATCH] Corrette variabili .env")

# 4. Installa librerie se mancano
REQUIRED_PKGS = [
    "python-telegram-bot==22.1", "flask", "stripe", "openai", "apscheduler", "python-dotenv",
    "SQLAlchemy", "unittest2", "scikit-learn", "transformers", "requests", "beautifulsoup4",
    "selenium", "reportlab", "PyPDF2", "Pillow", "pandas", "numpy", "SpeechRecognition", "pyttsx3",
    "streamlit", "tqdm", "Werkzeug", "aiohttp", "qrcode", "webpush", "pytz", "lxml"
]
def pip_install_missing():
    for pkg in REQUIRED_PKGS:
        pkg_name = pkg.split("==")[0] if "==" in pkg else pkg
        try:
            __import__(pkg_name)
        except Exception:
            print(f"[LIB] Installa {pkg} ...")
            subprocess.run([sys.executable, "-m", "pip", "install", pkg])

# 5. Patcha tutti i file .py principali
def patch_all_py():
    for root, dirs, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith(".py") and "venv" not in root and "site-packages" not in root and "backup" not in root:
                fix_imports_py(os.path.join(root, file))

if __name__ == "__main__":
    print("="*50)
    print("MASSIMO AI - AUTO PULIZIA E AUTOFIX 🚀")
    print("="*50)
    backup_files()
    fix_env()
    pip_install_missing()
    patch_all_py()
    print("==================================================")
    print("✅ Tutto pulito! Ora puoi lanciare main.py senza pensieri.")
    print("==================================================")
    print("Esempio: (venv attivo) python main.py")

    # Avvio main.py se vuoi farlo subito!
    # try:
    #     subprocess.run([sys.executable, "main.py"])
    # except Exception as e:
    #     print(f"[ERRORE AVVIO main.py]: {e}")
async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
