"""
FACTORY – Generatore oggetti mondi/agent, plug-in, audit hook.
"""
def create_object(object_type: str, data: dict):
    import logging
    id_gen = f"{object_type[:1].upper()}-{abs(hash(data.get('nome','x'))) % 10**6}"
    obj = {"id": id_gen, **data}
    logging.info(f"[FACTORY] Creato {object_type}: {id_gen}")
    # TODO: Hook/audit event, plugin
    return obj
