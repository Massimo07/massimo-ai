from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import logging, os, traceback

# Carica .env
load_dotenv()

# ========== LOGGING ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger("MassimoAI-Main")

# ========== APP SETUP ==========
app = FastAPI(
    title="Massimo AI – AI Factory Universe",
    description="La piattaforma AI più avanzata e generativa del mondo. Mondi verticali, pagamenti, dashboard, automazioni, memory, onboarding, branding, notifiche e molto altro.",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ========== CORS (MULTI-PIATTAFORMA, MULTI-CANALE) ==========
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "https://tuodominio.com",
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== IMPORTA E COLLEGA TUTTI I ROUTER ==========
try:
    from backend.mondi_factory_module import router as mondi_router
    from backend.branding_module import router as branding_router
    from backend.onboarding_universale import router as onboarding_uni_router
    from backend.onboarding_smart import router as onboarding_smart_router
    from backend.ai_factory_autogen import router as ai_factory_router
    from backend.landing_module import router as landing_router
    from backend.stripe_module import router as stripe_router
    from backend.memory_module import router as memory_router
    from backend.dashboard_module import router as dashboard_router
    from backend.livelli_module import router as livelli_router
    from backend.notification_module import router as notification_router
    from backend.voice_module import router as voice_router
except Exception as e:
    logger.error("Errore nell'importazione dei router: %s", e)
    raise

app.include_router(mondi_router)
app.include_router(branding_router)
app.include_router(onboarding_uni_router)
app.include_router(onboarding_smart_router)
app.include_router(ai_factory_router)
app.include_router(landing_router)
app.include_router(stripe_router)
app.include_router(memory_router)
app.include_router(dashboard_router)
app.include_router(livelli_router)
app.include_router(notification_router)
app.include_router(voice_router)

# ========== HEALTHCHECK E ROOT ==========
@app.get("/", tags=["Sistema"])
async def root():
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["Sistema"])
async def healthcheck():
    return {"status": "ok", "version": app.version, "environment": os.getenv("ENV", "dev")}

# ========== ERROR HANDLER GLOBALE (PERFEZIONE ABSOLUTA) ==========
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error("Errore non gestito: %s\nTraceback:\n%s", exc, traceback.format_exc())
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": f"Errore interno MassimoAI: {str(exc)}"},
    )

# ========== HOOK STARTUP/SHUTDOWN ==========
@app.on_event("startup")
async def on_startup():
    logger.info("🚀 Massimo AI è pronto: ogni modulo è attivo e generativo.")

@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Massimo AI è stato spento con successo.")

# ========== METADATA FUTURE PROOF ==========
# Aggiungi qui meta/future endpoint, versionamento, upgrade route, ecc.
