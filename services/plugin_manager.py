class PluginManager:
    def __init__(self):
        self.plugins = {}
    def install(self, name, plugin):
        self.plugins[name] = plugin
    def uninstall(self, name):
        self.plugins.pop(name, None)
    def run(self, name, *args, **kwargs):
        if name in self.plugins:
            return self.plugins[name](*args, **kwargs)
        raise Exception("Plugin non trovato")
plugin_manager = PluginManager()
