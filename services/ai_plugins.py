from ai_engine.engine import ai_engine

def generate_ai_response(plugin, prompt, context=None):
    return ai_engine.run(plugin, prompt, context)
