from telegram.ext import ContextTypes, ContextTypes
import os
import sys
import subprocess
import shutil
import glob

######################
# CONFIGURAZIONE BASE
######################
REQUIREMENTS = [
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
FOLDERS = ["logs", "data", "images", "backups", "src"]

def print_head():
    print("🚀 [MASSIMO AI SETUP] Avvio della Formula 1 della tua AI...")
    print("="*60)

def ensure_venv():
    if not os.path.exists("venv"):
        print("⚠️  Ambiente virtuale mancante: CREAZIONE...")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
    else:
        print("🟢 Ambiente virtuale 'venv' già presente.")

def activate_venv():
    if os.name == "nt":
        return os.path.join("venv", "Scripts", "python.exe")
    else:
        return os.path.join("venv", "bin", "python")

def pip_upgrade(python_bin):
    subprocess.run([python_bin, "-m", "pip", "install", "--upgrade", "pip"], check=True)

def pip_install_all(python_bin):
    # Crea requirements.txt
    with open("requirements.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(REQUIREMENTS) + "\n")
    print("🔄 Installazione TUTTI i pacchetti necessari...")
    subprocess.run([python_bin, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

def ensure_folders():
    for folder in FOLDERS:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"📁  Cartella '{folder}' creata.")
        else:
            print(f"🟢 Cartella '{folder}' presente.")

def clean_pycache():
    print("🧹 Pulizia cache e file temporanei...")
    for root, dirs, files in os.walk("."):
        for d in dirs:
            if d == "__pycache__":
                try:
                    shutil.rmtree(os.path.join(root, d))
                    print(f"  - Eliminato: {os.path.join(root, d)}")
                except Exception: pass

def check_env_file():
    if not os.path.exists(".env"):
        with open(".env", "w", encoding="utf-8") as f:
            f.write("# Qui puoi inserire le variabili d'ambiente!\n")
            f.write("TELEGRAM_TOKEN=INSERISCI_TOKEN_QUI\n")
            f.write("OPENAI_API_KEY=INSERISCI_OPENAI_KEY\n")
            f.write("LIVEONPLUS_USER=maxmarfisi@gmail.com\n")
            f.write("LIVEONPLUS_PASSWORD=Ma551m07.\n")
            f.write("LIVEON_USER=LOP906892IT\n")
            f.write("LIVEON_PASS=Ma551m07.\n")
        print("⚠️  File .env creato! Ricordati di completare i dati.")
    else:
        print("🟢 File .env già presente.")

def patch_import_filters():
    print("🔧 Fix automatico import 'Filters' -> 'filters' e path...")
    for pyfile in glob.glob("**/*.py", recursive=True):
        if "venv" in pyfile or "site-packages" in pyfile: continue
        try:
            with open(pyfile, "r", encoding="utf-8") as f:
                code = f.read()
            orig = code
            code = code.replace("from telegram.ext import filters", "from telegram.ext import filters"), ContextTypes
            code = code.replace("filters.", "filters.")
            # Altri fix puoi aggiungerli qui...
            if code != orig:
                with open(pyfile, "w", encoding="utf-8") as f:
                    f.write(code)
                print(f"  - Patchato: {pyfile}")
        except Exception as e:
            print(f"  ⚠️  Errore patchando {pyfile}: {e}")

def patch_encoding_utf8():
    print("🔧 Fix encoding UTF-8 su tutti i file .py...")
    for pyfile in glob.glob("**/*.py", recursive=True):
        if "venv" in pyfile or "site-packages" in pyfile: continue
        try:
            with open(pyfile, "rb") as f:
                content = f.read()
            # Prova a decodificare, se errore riscrive in utf-8 ignorando errori
            try:
                content.decode("utf-8")
            except UnicodeDecodeError:
                fixed = content.decode("latin-1").encode("utf-8")
                with open(pyfile, "wb") as f:
                    f.write(fixed)
                print(f"  - Riconvertito: {pyfile}")
        except Exception as e:
            print(f"  ⚠️  Errore encoding {pyfile}: {e}")

def main():
    print_head()
    ensure_venv()
    python_bin = activate_venv()
    pip_upgrade(python_bin)
    pip_install_all(python_bin)
    ensure_folders()
    clean_pycache()
    check_env_file()
    patch_import_filters()
    patch_encoding_utf8()
    print("="*60)
    print("🎉 **TUTTO AUTOMATIZZATO!**")
    print("✅ Ora lancia il tuo main.py (da src) e... ***VOLAAAAAA!*** 🚀")

if __name__ == "__main__":
    main()