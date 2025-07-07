# ai_generator.py
"""
AI Generator: crea mondi verticali Massimo AI da zero. Branding, struttura cartelle, plugin, livelli, dashboard.
Ogni settore, ogni lingua, zero limiti.
"""

import os

class AIGenerator:
    def __init__(self, base_dir="massimo_worlds"):
        self.base_dir = base_dir

    def create_world(self, world_name, features, plugins, branding, levels=None):
        # Crea cartelle base mondo
        world_path = os.path.join(self.base_dir, world_name)
        os.makedirs(world_path, exist_ok=True)
        # Sottocartelle e moduli
        for f in features:
            os.makedirs(os.path.join(world_path, f), exist_ok=True)
        # Plugin
        plugin_dir = os.path.join(world_path, "plugins_ai")
        os.makedirs(plugin_dir, exist_ok=True)
        for p in plugins:
            with open(os.path.join(plugin_dir, f"{p}.py"), "w", encoding="utf-8") as fp:
                fp.write(f"# Plugin placeholder: {p}\n")
        # Branding (logo, claim, payoff)
        with open(os.path.join(world_path, "branding.txt"), "w", encoding="utf-8") as bf:
            bf.write(f"Nome: {branding['name']}\nClaim: {branding['claim']}\nPayoff: {branding['payoff']}\n")
        # Livelli (se presenti)
        if levels:
            with open(os.path.join(world_path, "levels.json"), "w", encoding="utf-8") as lf:
                import json
                json.dump(levels, lf, ensure_ascii=False, indent=2)
        return f"Mondo '{world_name}' creato con successo!"

# ESEMPIO USO:
# gen = AIGenerator()
# gen.create_world("FormazioneDocenti", ["dashboard", "corsi", "community"], ["ai_content", "ai_quiz"], {"name":"Formazione Docenti AI", "claim":"Insegna. Impara. Evolvi.", "payoff":"Il futuro dell’educazione."})
