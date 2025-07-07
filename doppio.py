import os

project_root = "massimo_ai_neuro"  # Sostituisci con il percorso completo
all_files = {}

for root, dirs, files in os.walk(project_root):
    for f in files:
        if f.endswith('.py'):
            if f not in all_files:
                all_files[f] = []
            all_files[f].append(os.path.join(root, f))

for name, paths in all_files.items():
    if len(paths) > 1:
        print(f"DOPPIONE: {name}")
        for p in paths:
            print("  ->", p)
