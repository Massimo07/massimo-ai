from telegram.ext import ContextTypes, ContextTypes
import os
import sys
import subprocess
import shutil
import glob
from pathlib import Path

# 1. PATCHA IMPORTS: sostituisce "Filters" con "filters" (Python Telegram Bot >13)
def patch_imports(root='.'):
    for path in Path(root).rglob('*.py'):
        try:
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()
            new_code = code.replace("from telegram.ext import filters", "from telegram.ext import filters"), ContextTypes
            new_code = new_code.replace("filters.", "filters.")
            if new_code != code:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_code)
                print(f"✅ PATCHATO: {path}")
        except Exception as e:
            print(f"⚠️ ERRORE SU {path}: {e}")

# 2. CONTROLLA E CREA .env.example
def check_env():
    example_vars = [
        "TELEGRAM_TOKEN=", "OPENAI_API_KEY=", "STRIPE_KEY=", "LIVEONPLUS_USER=", "LIVEONPLUS_PASSWORD=",
        "LIVEON_USER=", "LIVEON_PASS="
    ]
    env_path = Path(".env")
    example_path = Path(".env.example")
    if not env_path.exists():
        print("⚠️ File .env NON TROVATO! Creazione .env.example...")
        with open(example_path, "w", encoding="utf-8") as f:
            f.write("\n".join(example_vars))
    else:
        with open(env_path, "r", encoding="utf-8") as f:
            content = f.read()
        for var in example_vars:
            if var.split("=")[0] not in content:
                print(f"⚠️ Variabile mancante: {var}")
                with open(example_path, "a", encoding="utf-8") as f:
                    f.write(f"{var}\n")

# 3. INSTALLA DIPENDENZE (requirements.txt)
def install_requirements():
    req = Path("requirements.txt")
    if req.exists():
        print("🔄 Controllo/installa dipendenze da requirements.txt...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        except Exception as e:
            print("⚠️ Errore installazione requirements:", e)
    else:
        print("⚠️ requirements.txt NON TROVATO!")

# 4. CREA CARTELLE ESSENZIALI
def make_dirs():
    for d in ["logs", "data", "corsi"]:
        Path(d).mkdir(exist_ok=True)
    print("📁 Cartelle essenziali pronte (logs, data, corsi).")

# 5. AUTOGENERA TEMPLATE CORSI
def auto_create_corsi():
    base = Path("corsi")
    base.mkdir(exist_ok=True)
    corsi_default = ["livello1_base.md", "livello2_cambio_vita.md", "livello3_mentalita.md"]
    for corso in corsi_default:
        p = base / corso
        if not p.exists():
            with open(p, "w", encoding="utf-8") as f:
                f.write(f"# {corso.replace('_', ' ').title()}\n\n- Step 1: \n- Step 2: \n- Quiz:\n")
            print(f"📝 Template creato: {corso}")

# 6. AVVIA MAIN.PY
def avvia_main():
    print("🚀 AVVIO Massimo AI: main.py")
    subprocess.run([sys.executable, "main.py"])

if __name__ == "__main__":
    print("\n💥 PATCH E AVVIO MASSIMO AI (FULL AUTO MODE)\n")
    patch_imports(".")
    check_env()
    install_requirements()
    make_dirs()
    auto_create_corsi()
    avvia_main()