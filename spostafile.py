import os
import shutil

SOURCE_DIR = "to_sort"
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

RULES = [
    ("voice", "voice"),
    ("Telegram", "telegram"),
    ("user", "moduli_ai"),
    ("profilo", "moduli_ai"),
    ("notifica", "services"),
    ("webhook", "services"),
    ("push", "services"),
    ("utils", "utils"),
    ("VR", "moduli_ai"),
    ("vision_board", "moduli_ai"),
    # ...aggiungi le tue regole personalizzate!
]

def decide_dest_by_content(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read(2000)  # Legge solo le prime 2000 lettere per velocità
            for keyword, folder in RULES:
                if keyword.lower() in content.lower():
                    return folder
    except Exception as e:
        print(f"Impossibile leggere {filepath}: {e}")
    return None

for filename in os.listdir(os.path.join(PROJECT_ROOT, SOURCE_DIR)):
    src_path = os.path.join(PROJECT_ROOT, SOURCE_DIR, filename)
    if not os.path.isfile(src_path) or not filename.endswith(".py"):
        continue
    folder = decide_dest_by_content(src_path)
    if folder:
        os.makedirs(os.path.join(PROJECT_ROOT, folder), exist_ok=True)
        dst_path = os.path.join(PROJECT_ROOT, folder, filename)
        shutil.move(src_path, dst_path)
        print(f"{filename} spostato in {folder}/ (per contenuto)")
    else:
        print(f"{filename} non corrisponde a nessuna regola di contenuto, resta in to_sort/")
