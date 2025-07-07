"""
Analytics API – Dashboard dati, esportazione, alert, audit.
"""

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
import logging

router = APIRouter()

class AnalyticsData(BaseModel):
    metric: str
    value: float
    timestamp: str

ANALYTICS = [
    AnalyticsData(metric="users", value=1234, timestamp="2024-07-06T23:00:00Z"),
    AnalyticsData(metric="payments", value=220, timestamp="2024-07-06T23:00:00Z"),
]

def get_current_user():
    return {"user_id": "admin"}

@router.get("/", response_model=List[AnalyticsData])
def get_analytics(current=Depends(get_current_user)):
    logging.info(f"[analytics] Accesso dashboard da {current['user_id']}")
    return ANALYTICS
