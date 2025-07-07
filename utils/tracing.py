import uuid
from fastapi import Request

async def add_request_id(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response

# Come usarlo:
# app.middleware("http")(add_request_id)
# Poi in logger: logger.info(f"ReqID={request.state.request_id} ...")
# Pronto per tracing distribuito/analytics/monitoraggio!
