from telegram.ext import CommandHandler
from telegram.ext import ContextTypes, ContextTypes
import os
import shutil
import subprocess
import sys
import time

def banner(msg):
    print("=" * 60)
    print(f"{msg}")
    print("=" * 60)

def clean_venv():
    venv_path = os.path.join(os.getcwd(), "venv")
    if os.path.exists(venv_path):
        print("🧹 Rimozione vecchio virtualenv (venv)...")
        shutil.rmtree(venv_path)
        time.sleep(1)
    else:
        print("ℹ️ Nessun venv da rimuovere.")

def create_venv():
    print("🐍 Creazione nuovo virtualenv...")
    subprocess.check_call([sys.executable, "-m", "venv", "venv"])

def activate_venv():
    # Su Windows usa Scripts, su Mac/Linux bin
    if os.name == "nt":
        activate = ".\\venv\\Scripts\\activate"
    else:
        activate = "source venv/bin/activate"
    return activate

def pip_install_upgrade():
    print("⬆️  Aggiornamento pip, setuptools, wheel...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])

def install_requirements():
    req_path = "requirements.txt"
    if not os.path.exists(req_path):
        print("⚠️  requirements.txt non trovato, lo genero base...")
        with open(req_path, "w") as f:
            f.write("""python-telegram-bot==22.1
flask==3.0.3
stripe==12.2.0
openai==1.30.1
apscheduler==3.10.4
python-dotenv==1.0.1
SQLAlchemy==2.0.30
unittest2==1.1.0
scikit-learn==1.4.2
transformers==4.41.2
requests==2.31.0
beautifulsoup4==4.12.3
selenium==4.21.0
reportlab==4.1.0
PyPDF2==3.0.1
Pillow==10.3.0
pandas==2.2.2
numpy==1.26.4
SpeechRecognition==3.10.1
pyttsx3==2.90
streamlit==1.35.0
tqdm==4.66.4
Werkzeug==3.0.3
aiohttp==3.9.5
qrcode==7.4.2
webpush==1.0.2
pytz==2024.1
lxml==5.2.2""")
    print("📦 Installazione librerie (requirements.txt)...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_path])

def patch_imports():
    # Esempio di patch automatica per 'Filters' e altri import
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, encoding="utf-8", errors="ignore") as f:
                    txt = f.read()
                patched = txt.replace("from telegram.ext import filters", "from telegram.ext import filters"), ContextTypes
                patched = patched.replace("filters.", "filters.")
                if patched != txt:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(patched)
    print("🔧 Import patchati automaticamente (Filters, etc)")

def launch_main():
    print("🚀 Avvio Massimo AI (main.py)...")
    try:
        subprocess.check_call([sys.executable, "main.py"])
    except subprocess.CalledProcessError as e:
        print(f"❌ Errore di avvio: {e}")
        print("Controlla sopra per il traceback!")

def main():
    banner("MASSIMO AI - SETUP UNIVERSALE")
    answer = input("Vuoi ELIMINARE e ricreare venv (consigliato per errori pip)? [y/n]: ").lower()
    if answer.startswith("y"):
        clean_venv()
        create_venv()
        print(f"👉 Adesso attiva il venv: {activate_venv()} (poi premi INVIO)")
        input()
    pip_install_upgrade()
    install_requirements()
    patch_imports()
    launch_main()

if __name__ == "__main__":
    main()
async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
