"""
DASHBOARD – Aggrega stats, trend, export, healthcheck, alert.
"""
from typing import Dict, Any
import datetime

def get_dashboard_stats() -> Dict[str, Any]:
    stats = {
        "utenti": 1320,
        "mondi": 115,
        "agenti": 49,
        "abbonamenti": 870,
        "feedback": 215,
        "timestamp": datetime.datetime.utcnow().isoformat(),
    }
    return stats

def export_stats_csv(stats: Dict[str, Any]) -> str:
    header = ",".join(stats.keys())
    values = ",".join(str(v) for v in stats.values())
    return f"{header}\n{values}"

def trend_stats(period: int = 7) -> Dict[str, Any]:
    # Dummy trend: reale = query DB + analytics!
    return {"utenti_giornalieri": [10,12,13,15,17,20,25][:period]}
