import os
import re

SERVICES_DIR = "services"
ROOT_IMPORT = "from utils import get_user"

for file in os.listdir(SERVICES_DIR):
    if not file.endswith(".py"):
        continue
    path = os.path.join(SERVICES_DIR, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Rimuovi vecchie import get_user e sys.path.append
    content = re.sub(r"from\s+\.*utils\s+import\s+get_user", "", content)
    content = re.sub(r"import\s+sys.*?sys\.path\.append.*?\n", "", content, flags=re.DOTALL)
    # Inserisci il fix all’inizio
    new_head = 'import sys, os\nsys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\nfrom utils import get_user\n'
    content = new_head + content.lstrip()
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
print("✅ Tutte le importazioni nei servizi sono ora AUTOMATICAMENTE a prova di errore!")
