"""
core/__init__.py – Init avanzato con auto-scan
"""
import os
import glob

__all__ = []

# Autoload di tutti i file Python (tranne __init__)
module_path = os.path.dirname(__file__)
for file in glob.glob(os.path.join(module_path, "*.py")):
    base = os.path.basename(file)
    if base != "__init__.py":
        modname = base[:-3]
        __all__.append(modname)
