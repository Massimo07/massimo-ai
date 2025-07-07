import os
import re
from collections import defaultdict

# Configurazione
EXCLUDE_DIRS = {'venv', '__pycache__', 'backup', 'logs', 'data'}
OUTPUT_FILE = "unione_moduli.py"

def get_py_files(root):
    py_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for filename in filenames:
            if filename.endswith('.py'):
                py_files.append(os.path.join(dirpath, filename))
    return py_files

def extract_functions(filepath):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        code = f.read()
    matches = list(re.finditer(r'(def\s+[a-zA-Z0-9_]+\s*\([^\)]*\)\s*:[\s\S]+?)(?=\ndef\s|\Z)', code))
    return [(m.group(), m.group().split('(')[0].replace('def','').strip()) for m in matches]

if __name__ == "__main__":
    root = os.path.abspath(os.path.dirname(__file__))
    files = get_py_files(root)
    functions_by_name = defaultdict(list)
    already_written = set()

    # Estrae tutte le funzioni da tutti i file
    for file in files:
        try:
            for func_code, func_name in extract_functions(file):
                functions_by_name[func_name].append((file, func_code.strip()))
        except Exception as e:
            print(f"Errore su {file}: {e}")

    # Scrive il file di unione
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("# =============== SUPER UNIONE DI TUTTI I MODULI ===============\n\n")
        for func, all_defs in functions_by_name.items():
            if len(all_defs) == 1:
                # Funzione unica → scrivila normalmente
                file, code = all_defs[0]
                out.write(f"# Da: {os.path.relpath(file, root)}\n")
                out.write(code + "\n\n")
            else:
                # Funzione doppia o multipla → scrivi tutte le versioni
                out.write(f"# === FUSIONE: '{func}' trovata in {len(all_defs)} file ===\n")
                for idx, (file, code) in enumerate(all_defs, 1):
                    out.write(f"# Versione {idx} da: {os.path.relpath(file, root)}\n")
                    out.write(code + "\n\n")
                out.write("# === FINE FUSIONE ===\n\n")

    print(f"\nFatto! Tutte le funzioni fuse nel file: {OUTPUT_FILE}")
    print("Controlla le versioni multiple commentate e scegli la migliore manualmente dove necessario.")
