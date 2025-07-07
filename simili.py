import os
import re
from collections import defaultdict

# Cartelle da ignorare (puoi aggiungere venv, backup, ecc.)
EXCLUDE_DIRS = {'venv', '__pycache__', 'backup', 'logs', 'data'}

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
    # Regex per trovare tutte le funzioni (def nome_funzione(
    return re.findall(r'def\s+([a-zA-Z0-9_]+)\s*\(', code)

if __name__ == "__main__":
    root = os.path.abspath(os.path.dirname(__file__))
    files = get_py_files(root)
    funzioni = defaultdict(list)

    for file in files:
        try:
            for func in set(extract_functions(file)):
                funzioni[func].append(file)
        except Exception as e:
            print(f"Errore su {file}: {e}")

    print("\n=== FUNZIONI DOPPIE O SIMILI NEI VARI FILE ===\n")
    for func, filelist in funzioni.items():
        if len(filelist) > 1:
            print(f"FUNZIONE '{func}' trovata in:")
            for f in filelist:
                print(f"  - {os.path.relpath(f, root)}")
            print("---")
