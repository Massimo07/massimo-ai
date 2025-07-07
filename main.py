import pkgutil
import importlib
import os
import sys
import inspect

EXCLUDE = {'venv', '__pycache__', 'logs', 'data', 'assets', 'images'}

def trova_moduli(base_path):
    moduli = []
    for finder, name, ispkg in pkgutil.iter_modules([base_path]):
        if name not in EXCLUDE:
            moduli.append(name)
    return moduli

def importa_moduli_e_funzioni(base_path):
    sys.path.insert(0, base_path)
    moduli = trova_moduli(base_path)
    funzioni = {}
    for mod_name in moduli:
        try:
            mod = importlib.import_module(mod_name)
            print(f"✅ Modulo importato: {mod_name}")
            for nome, oggetto in inspect.getmembers(mod):
                if inspect.isfunction(oggetto) and not nome.startswith("_"):
                    funzioni[f"{mod_name}.{nome}"] = oggetto
        except Exception as e:
            print(f"❌ Errore importando {mod_name}: {e}")
    return funzioni

def menu(funzioni):
    chiavi = list(funzioni.keys())
    while True:
        print("\n=== FUNZIONI DISPONIBILI ===")
        for i, nome in enumerate(chiavi):
            print(f"{i+1}. {nome}")
        scelta = input("\nScegli una funzione da lanciare (numero, 'exit' per uscire): ")
        if scelta.lower() == 'exit':
            break
        try:
            idx = int(scelta) - 1
            if 0 <= idx < len(chiavi):
                print(f"\nEseguo: {chiavi[idx]}")
                try:
                    funzioni[chiavi[idx]]()
                except Exception as ex:
                    print(f"Errore durante l'esecuzione: {ex}")
            else:
                print("Numero non valido.")
        except:
            print("Input non valido.")

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    funzioni = importa_moduli_e_funzioni(base_path)
    menu(funzioni)
