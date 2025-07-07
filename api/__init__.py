"""
Modulo API – Router centrale e import endpoint.
"""

from fastapi import APIRouter

from .users import router as users_router
from .worlds import router as worlds_router
from .agents import router as agents_router
from .subscriptions import router as subscriptions_router
from .payments import router as payments_router
from .automation import router as automation_router
from .analytics import router as analytics_router
from .token import router as token_router
from .event import router as event_router
from .feedback import router as feedback_router
from .notifications import router as notifications_router

api_router = APIRouter()

api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(worlds_router, prefix="/worlds", tags=["worlds"])
api_router.include_router(agents_router, prefix="/agents", tags=["agents"])
api_router.include_router(subscriptions_router, prefix="/subscriptions", tags=["subscriptions"])
api_router.include_router(payments_router, prefix="/payments", tags=["payments"])
api_router.include_router(automation_router, prefix="/automation", tags=["automation"])
api_router.include_router(analytics_router, prefix="/analytics", tags=["analytics"])
api_router.include_router(token_router, prefix="/token", tags=["token"])
api_router.include_router(event_router, prefix="/event", tags=["event"])
api_router.include_router(feedback_router, prefix="/feedback", tags=["feedback"])
api_router.include_router(notifications_router, prefix="/notifications", tags=["notifications"])
