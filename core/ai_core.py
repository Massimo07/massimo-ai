"""
AI_CORE – Orchestrazione pipeline AI, multi-modello, explain, audit.
"""
def run_ai(input_data, model_name="gpt-4o"):
    from ai_engine.pipeline import predict
    # Log ogni predict con traceID
    import uuid, logging
    trace_id = str(uuid.uuid4())
    logging.info(f"[AI_CORE][{trace_id}] predict chiamata: model={model_name}")
    result = predict(input_data, model_name=model_name)
    result['trace_id'] = trace_id
    return result
