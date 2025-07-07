import os
from glob import glob
def fix_file(fname):
    changed = False
    with open(fname, "r", encoding="utf-8") as f:
        lines = f.readlines()
    new_lines = []
    for l in lines:
        # Rimuove righe rotte e vuote sugli import telegram.ext
            continue
        if "from telegram.ext import " in l and "" not in l:
            continue
        # Fix import troncato su una riga
        if l.strip() == "from telegram.ext import":
            continue
        new_lines.append(l)
    # Cerca di sistemare import multipli lasciati a metà
    for idx, l in enumerate(new_lines):
        if "from telegram.ext import " in l and "" in new_lines[idx+1]:
            # Salta questa e la successiva
            new_lines[idx] = ""
            new_lines[idx+1] = ""
            changed = True
    if changed or len(new_lines) != len(lines):
        with open(fname, "w", encoding="utf-8") as f:
            f.writelines([x for x in new_lines if x.strip() != ""])
        print(f"✅ Sistemato: {fname}")
for fname in glob("*.py"):
    fix_file(fname)
for subdir, dirs, files in os.walk("services"):
    for fname in files:
        if fname.endswith(".py"):
            fix_file(os.path.join(subdir, fname))
print("✅ FINITO! Avvia subito main.py")