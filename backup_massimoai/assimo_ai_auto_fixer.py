from telegram.ext import ContextTypes, ContextTypes
import os
import re
import sys
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))

# 1. Fix import Filters → filters e tutti i principali errori comuni
def fix_imports(path):
    print("🔄 Correzione import...")
    for dirpath, _, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                fpath = os.path.join(dirpath, file)
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
                new_text = text
                new_text = re.sub(r'from telegram\.ext import Filters', 'from telegram.ext import filters', new_text), ContextTypes
                new_text = re.sub(r'import Filters', 'import filters', new_text)
                new_text = re.sub(r'from telegram\.ext import MessageHandler', 'from telegram.ext import MessageHandler', new_text), ContextTypes
                new_text = re.sub(r'from telegram\.ext import CommandHandler', 'from telegram.ext import CommandHandler', new_text), ContextTypes
                new_text = re.sub(r'from telegram\.ext import CallbackQueryHandler', 'from telegram.ext import CallbackQueryHandler', new_text), ContextTypes
                new_text = re.sub(r'from telegram\.ext import Updater', 'from telegram.ext import ApplicationBuilder', new_text), ContextTypes
                # Fix relative import errati
                new_text = re.sub(r'from \.\.utils import get_user', 'from utils import get_user', new_text)
                # ...aggiungi altri fix qui...
                if new_text != text:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(new_text)
                    print(f"✅ Patchato: {file}")

# 2. Ricostruzione handlers.py automatico
def rebuild_handlers(services_dir="services"):
    print("🔄 Ricostruzione automatica di handlers.py...")
    handler_lines = [
        "from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, filters",, ContextTypes
        "",
    ]
    found = 0
    for file in os.listdir(os.path.join(ROOT, services_dir)):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = file[:-3]
            handler_var = f"{module_name}_handler"
            handler_lines.append(f"from services.{module_name} import {handler_var}")
            found += 1
    handler_lines.append("")
    handler_lines.append("def get_handlers():")
    for file in os.listdir(os.path.join(ROOT, services_dir)):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = file[:-3]
            handler_var = f"{module_name}_handler"
            handler_lines.append(f"    yield {handler_var}")
    code = "\n".join(handler_lines)
    with open(os.path.join(ROOT, "handlers.py"), "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ handlers.py aggiornato ({found} handler trovati)")

# 3. Aggiorna requirements.txt con moduli importati non ancora elencati
def update_requirements(path):
    print("🔄 Aggiornamento requirements.txt...")
    pkgs = set()
    for dirpath, _, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(dirpath, file), "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        m = re.match(r'import (\w+)', line) or re.match(r'from (\w+)', line)
                        if m:
                            pkgs.add(m.group(1))
    base = {"os","re","sys","subprocess","time","json","logging","threading"}
    stdlibs = base | {"csv","typing"}
    pkgs = [p for p in pkgs if p not in stdlibs]
    with open(os.path.join(ROOT, "requirements.txt"), "a", encoding="utf-8") as f:
        for p in pkgs:
            f.write(f"{p}\n")
    print("✅ requirements.txt aggiornato")

# 4. Controlla variabili d’ambiente fondamentali
def check_env(required_vars=["TELEGRAM_TOKEN","OPENAI_API_KEY"]):
    print("🔎 Controllo variabili d'ambiente (.env)...")
    if not os.path.exists(os.path.join(ROOT, ".env")):
        print("❌ File .env NON trovato!")
        return
    with open(os.path.join(ROOT, ".env"),"r",encoding="utf-8") as f:
        data = f.read()
    for var in required_vars:
        if var not in data:
            print(f"⚠️  Variabile mancante: {var}")

# 5. Patch encoding (UTF-8) se serve (opzionale)
def patch_encoding(path):
    print("🔄 Patch encoding (UTF-8)...")
    for dirpath, _, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                fpath = os.path.join(dirpath, file)
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        f.read()
                except:
                    try:
                        with open(fpath, "r", encoding="latin1") as f:
                            text = f.read()
                        with open(fpath, "w", encoding="utf-8") as f:
                            f.write(text)
                        print(f"✅ {file} convertito in UTF-8")
                    except:
                        print(f"❌ {file} NON convertito (errore encoding)")

# 6. Lancia main.py alla fine
def run_main():
    print("🚦 Avvio di main.py...")
    subprocess.run([sys.executable, "main.py"])

if __name__ == "__main__":
    print("🚀 MASSIMO AI AUTO-FIXER AVVIATO")
    patch_encoding(ROOT)
    fix_imports(ROOT)
    rebuild_handlers("services")
    update_requirements(ROOT)
    check_env(["TELEGRAM_TOKEN","OPENAI_API_KEY","LIVEONPLUS_USER","LIVEONPLUS_PASSWORD","LIVEON_USER","LIVEON_PASS"])
    print("✅ TUTTO PATCHATO! Puoi ora lanciare main.py — oppure premo [INVIO] per avviarlo subito!")
    input()
    run_main()