from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from time import time
from collections import defaultdict

# In memory: adatto a sviluppo e istanza singola
rate_limits = defaultdict(list)  # {key: [timestamps]}

class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 100, period: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.period = period

    async def dispatch(self, request: Request, call_next):
        # Usa user_id se autenticato, altrimenti IP
        user = getattr(request.state, 'user', None)
        key = user.id if user else request.client.host

        now = time()
        window_start = now - self.period
        timestamps = rate_limits[key]
        # Elimina timestamp vecchi
        rate_limits[key] = [ts for ts in timestamps if ts > window_start]
        if len(rate_limits[key]) >= self.max_requests:
            raise HTTPException(status_code=429, detail="Troppe richieste – riprova più tardi.")
        rate_limits[key].append(now)
        return await call_next(request)

# Come aggiungerlo:
# from utils.rate_limiter import RateLimiterMiddleware
# app.add_middleware(RateLimiterMiddleware, max_requests=30, period=60)  # 30 richieste/minuto

# Per produzione, usa Redis e aiuta la scalabilità multi-server!
