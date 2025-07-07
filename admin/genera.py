import os

# Cartelle da ESCLUDERE dalla scansione
EXCLUDE_DIRS = ['venv', 'backup', 'logs', 'tests', 'data', 'database', 'assets', '__pycache__']

# Directory di partenza (root del tuo progetto)
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

imports = []
modules_map = {}

for root, dirs, files in os.walk(ROOT_DIR):
    # Escludi directory inutili
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    for file in files:
        if file.endswith('.py') and file != 'main.py' and not file.startswith('__'):
            # Percorso relativo
            rel_dir = os.path.relpath(root, ROOT_DIR).replace("\\", ".").replace("/", ".")
            module_name = file[:-3]
            if rel_dir == ".":
                import_stmt = f"import {module_name}"
                modules_map[module_name] = module_name
            else:
                import_stmt = f"from {rel_dir} import {module_name}"
                modules_map[module_name] = f"{rel_dir}.{module_name}"
            imports.append(import_stmt)

# Stampa tutti gli import pronti
print("# === IMPORT AUTOGENERATI ===")
for imp in sorted(imports):
    print(imp)

# Stampa la mappa moduli (puoi copiarla nella tua classe centrale)
print("\n# === MAPPA MODULI PER main.py ===")
print("moduli = {")
for key, mod in modules_map.items():
    print(f'    "{key}": {mod},')
print("}")
