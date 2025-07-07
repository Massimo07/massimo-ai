import os
import re
import difflib
from collections import defaultdict

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
    # Match function name + content (non greedy)
    matches = list(re.finditer(r'(def\s+[a-zA-Z0-9_]+\s*\([^\)]*\)\s*:[\s\S]+?)(?=\ndef\s|\Z)', code))
    return [(m.group(), m.group().split('(')[0].replace('def','').strip()) for m in matches]

if __name__ == "__main__":
    root = os.path.abspath(os.path.dirname(__file__))
    files = get_py_files(root)
    functions_by_name = defaultdict(list)
    all_functions = []

    for file in files:
        try:
            for func_code, func_name in extract_functions(file):
                functions_by_name[func_name].append((file, func_code.strip()))
                all_functions.append((file, func_name, func_code.strip()))
        except Exception as e:
            print(f"Errore su {file}: {e}")

    print("\n=== FUNZIONI DOPPIE (STESSO NOME) ===\n")
    for func, filelist in functions_by_name.items():
        if len(filelist) > 1:
            print(f"FUNZIONE '{func}' trovata in:")
            for f, _ in filelist:
                print(f"  - {os.path.relpath(f, root)}")
            print("---")

    print("\n=== FUNZIONI “QUASI-UGUALI” (controllo similitudine) ===\n")
    checked = set()
    for i, (file1, name1, code1) in enumerate(all_functions):
        for j in range(i+1, len(all_functions)):
            file2, name2, code2 = all_functions[j]
            if (file1, file2, name1) in checked or name1 != name2:
                continue
            ratio = difflib.SequenceMatcher(None, code1, code2).ratio()
            if 0.7 < ratio < 1.0:  # puoi alzare/abbassare la soglia a piacere
                print(f"Funzione simile '{name1}':")
                print(f" - {os.path.relpath(file1, root)}")
                print(f" - {os.path.relpath(file2, root)}")
                print(f"   (similitudine: {ratio:.2f})")
                print("---")
            checked.add((file1, file2, name1))
