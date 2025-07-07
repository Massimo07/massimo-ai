import os

EXCLUDE = {'venv', '__pycache__'}

def crea_init(root):
    for dirpath, dirnames, filenames in os.walk(root):
        # Escludi cartelle inutili
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE]
        if '__init__.py' not in filenames:
            init_path = os.path.join(dirpath, '__init__.py')
            with open(init_path, "w", encoding="utf-8") as f:
                pass  # file vuoto
            print(f"Creato: {init_path}")

if __name__ == "__main__":
    root = os.path.abspath(os.path.dirname(__file__))
    crea_init(root)
    print("\n✅ Tutti i file __init__.py sono stati creati dove mancavano.")
