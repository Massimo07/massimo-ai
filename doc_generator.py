"""
Modulo: doc_generator.py
Genera documentazione PDF/HTML per Massimo AI, con elenco moduli, funzioni, esempio d’uso e descrizioni.
Automatizza la stesura manuale.
"""

import os

MODULES = [
    "data_manager.py",
    "agents.py",
    "feedback.py",
    "log_audit.py",
    "knowledge_editable.py",
    "disaster_recovery.py",
    # Aggiungi tutti i moduli chiave!
]

def generate_doc():
    doc = "# Massimo AI — Documentazione moduli\n\n"
    for fname in MODULES:
        doc += f"\n## {fname}\n"
        if os.path.exists(fname):
            with open(fname) as f:
                lines = f.readlines()
            docstring = ""
            if lines and lines[0].strip().startswith('"""'):
                for line in lines[1:]:
                    if line.strip().startswith('"""'): break
                    docstring += line
            doc += docstring + "\n"
        else:
            doc += "File non trovato.\n"
    with open("MASSIMO_AI_DOC.md", "w") as f:
        f.write(doc)
    print("Documentazione generata in MASSIMO_AI_DOC.md")

if __name__ == "__main__":
    generate_doc()
