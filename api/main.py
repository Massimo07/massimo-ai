# api/main.py
"""
MAIN API ENTRYPOINT – Avvio FastAPI, routing, healthcheck, error handler globale (Massimo AI)

- Routing automatico e modularità
- Healthcheck
- Logging startup/shutdown
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

from api.users import router as users_router
from api.feedback import router as feedback_router
from api.analytics import router as analytics_router
from api.payments import router as payments_router
from api.abtest import router as abtest_router
from api.agents import router as agents_router
from api.ai import router as ai_router
from api.automations import router as automations_router
from api.event import router as event_router
from api.factory import router as factory_router
from api.gamification import router as gamification_router
from api.invite import router as invite_router

logger = logging.getLogger("api.main")
logger.setLevel(logging.INFO)

app = FastAPI(title="Massimo AI – API TOP", version="1.0")

# Include router per tutte le API modulari
app.include_router(users_router)
app.include_router(feedback_router)
app.include_router(analytics_router)
app.include_router(payments_router)
app.include_router(abtest_router)
app.include_router(agents_router)
app.include_router(ai_router)
app.include_router(automations_router)
app.include_router(event_router)
app.include_router(factory_router)
app.include_router(gamification_router)
app.include_router(invite_router)

@app.get("/api/v1/healthz", tags=["system"])
def healthcheck():
    """Check di sistema pronto per deploy/cloud/test."""
    logger.info("[system] Healthcheck OK")
    return {"status": "ok", "message": "Massimo AI API viva!"}

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"[request] {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"[response] Status: {response.status_code}")
    return response

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"[error] Unhandled Exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Errore interno. Contatta l’admin."}
    )
