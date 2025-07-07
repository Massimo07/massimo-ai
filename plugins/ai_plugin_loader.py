# /plugins_ai/ai_plugin_loader.py

import os
import importlib

class AIPluginLoader:
    def __init__(self, plugin_dir="./plugins_ai"):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                modulename = filename[:-3]
                try:
                    module = importlib.import_module(f"plugins_ai.{modulename}")
                    self.plugins[modulename] = module
                except Exception as e:
                    print(f"Errore caricamento plugin {modulename}:", e)

    def get_plugin(self, name):
        return self.plugins.get(name, None)

# USO:
# loader = AIPluginLoader()
# loader.load_plugins()
# plugin = loader.get_plugin("ai_social_post_generator")
