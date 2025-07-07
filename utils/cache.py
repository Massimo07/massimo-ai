import functools
import time

# Semplice cache in memoria (per demo e dev)
_cache = {}

def cache_response(ttl: int = 60):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            key = (func.__name__, str(args), str(kwargs))
            now = time.time()
            if key in _cache and now - _cache[key]['time'] < ttl:
                return _cache[key]['value']
            result = await func(*args, **kwargs)
            _cache[key] = {'value': result, 'time': now}
            return result
        return wrapper
    return decorator

# Per produzione: sostituisci con redis.asyncio oppure aioredis
# Esempio di uso:
# @cache_response(ttl=120)
# async def get_home_stats(): ...
