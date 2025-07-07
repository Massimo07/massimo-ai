"""
utils/time.py – Utility gestione tempo, time zone, timestamp, friendly date.
"""
from datetime import datetime, timezone, timedelta

def now_utc() -> datetime:
    return datetime.now(timezone.utc)

def iso_format(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat()

def from_timestamp(ts: float) -> datetime:
    return datetime.fromtimestamp(ts, tz=timezone.utc)

def friendly_delta(dt: datetime) -> str:
    diff = now_utc() - dt
    if diff.days:
        return f"{diff.days} giorni fa"
    h = diff.seconds // 3600
    if h:
        return f"{h} ore fa"
    m = (diff.seconds % 3600) // 60
    if m:
        return f"{m} minuti fa"
    return "poco fa"
