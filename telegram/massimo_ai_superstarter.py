from telegram.ext import ContextTypes
from telegram.ext import CommandHandler
import os
import subprocess
import sys
import time

def run_python_script(script):
    print(f"[AUTO] Avvio {script} ...")
    p = subprocess.run([sys.executable, script])
    return p.returncode

def fix_all_py():
    import re
    print("[AUTO] Fix import multipli/indentazione...")
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py") and "venv" not in root and "site-packages" not in root and "backup" not in root:
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                fixed_lines = []
                inside = False
                imports = []
                for line in lines:
                    if re.match(r'^\s*from telegram.ext import \($', line):
                        inside = True; imports = []; continue
                    elif inside:
                        if ")" in line:
                            inside = False
                            allim = ', '.join(l.strip().strip(',') for l in imports if l.strip())
                            fixed_lines.append(f'from telegram.ext import {allim}\n')
                            continue
                        else: imports.append(line); continue
                    if re.match(r'^\s*[A-Za-z_0-9]+,\s*$', line):
                        continue
                    fixed_lines.append(line)
                with open(path, "w", encoding="utf-8") as f:
                    f.writelines(fixed_lines)
                print(f"[OK] Patchato: {path}")

if __name__ == "__main__":
    print("🛠️ [SUPERSTARTER] Fix di import e indentazione in corso...")
    fix_all_py()
    print("🟢 Fix completato! Avvio Massimo AI ...")
    time.sleep(1)
    exitcode = run_python_script("main.py")
    if exitcode == 0:
        print("✅ MASSIMO AI partito con successo!")
    else:
        print(f"❌ MASSIMO AI si è fermato con codice {exitcode}. Controlla i log e le prime righe di handlers.py.")

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")
