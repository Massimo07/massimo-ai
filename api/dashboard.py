# api/dashboard.py
from fastapi import APIRouter, Depends
from core.dashboard import get_dashboard_stats, export_stats_csv
from core.security import validate_token

router = APIRouter()

@router.get("/stats")
def dashboard_stats(token: str = Depends(validate_token)):
    return get_dashboard_stats()

@router.get("/export/csv")
def export_csv(token: str = Depends(validate_token)):
    stats = get_dashboard_stats()
    csv = export_stats_csv(stats)
    return {"csv": csv}
