"""
Massimo AI – Plugin Engine
Gestione plug-in esterni, mondi tematici, estensioni, moduli di terze parti.
"""
import importlib

class PluginEngine:
    def __init__(self):
        self.plugins = {}

    def register(self, name, path):
        mod = importlib.import_module(path)
        self.plugins[name] = mod

    def call(self, name, *args, **kwargs):
        if name in self.plugins and hasattr(self.plugins[name], "run"):
            return self.plugins[name].run(*args, **kwargs)
        else:
            raise Exception(f"Plugin {name} non trovato o non valido")

    def list_plugins(self):
        return list(self.plugins.keys())
