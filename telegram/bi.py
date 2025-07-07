"""
Modulo: bi.py
Business Intelligence & Analytics per Massimo AI.
Elabora, aggrega e visualizza dati chiave: PV personali e di gruppo, crescita team, engagement, churn, obiettivi raggiunti, leaderboard.
Pronto per dashboard live, esportazione e alert predittivi.
"""

import logging
from data_manager import get_all_users, get_user_data
from datetime import datetime
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def compute_team_kpi():
    """
    Calcola i KPI fondamentali per il team: PV, crescita, attivi/inattivi, churn, etc.
    """
    users = get_all_users()
    total_pv = sum(user.get("pv_mese", 0) for user in users)
    directors = sum(1 for user in users if user.get("level") == "Director")
    active = sum(1 for user in users if user.get("engagement", 0) > 10)
    churn = sum(1 for user in users if user.get("last_active") and (datetime.now() - user["last_active"]).days > 30)
    return {
        "total_pv": total_pv,
        "directors": directors,
        "active": active,
        "churn": churn,
        "user_count": len(users)
    }

def plot_growth_chart(history_data):
    """
    Genera un grafico della crescita del team nel tempo (matplotlib).
    """
    dates = [entry["date"] for entry in history_data]
    pv_values = [entry["pv_group"] for entry in history_data]
    plt.figure(figsize=(8,5))
    plt.plot(dates, pv_values, marker="o")
    plt.title("Crescita PV Gruppo")
    plt.xlabel("Data")
    plt.ylabel("PV di gruppo")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/pv_growth_chart.png")
    logger.info("Grafico crescita generato e salvato.")

def weekly_report():
    """
    Crea report settimanale per admin/leader, pronto da inviare su Telegram o dashboard.
    """
    kpi = compute_team_kpi()
    report = (
        f"📈 Report Settimanale Massimo AI\n\n"
        f"PV Totali: {kpi['total_pv']}\n"
        f"Director attivi: {kpi['directors']}\n"
        f"Utenti attivi: {kpi['active']}/{kpi['user_count']}\n"
        f"Churn (utenti persi): {kpi['churn']}\n"
    )
    return report

def nps_score():
    """
    Calcola NPS interno (Net Promoter Score, soddisfazione team).
    """
    users = get_all_users()
    votes = [user.get("nps") for user in users if user.get("nps") is not None]
    if not votes:
        return 0
    promoters = sum(1 for v in votes if v >= 9)
    detractors = sum(1 for v in votes if v <= 6)
    nps = ((promoters - detractors) / len(votes)) * 100
    return nps

# --- Esempio di utilizzo ---
if __name__ == "__main__":
    print(weekly_report())
    print(f"NPS: {nps_score()}")
