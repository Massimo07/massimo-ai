"""
Modulo: dashboard.py
Generazione dashboard per utenti/admin: mostra avanzamento, statistiche, badge, leaderboard, report settimanali, NPS.
Pronto per esportazione (CSV, Excel, PDF), invio via Telegram o su web.
Integrazione diretta con BI, Gamification, CRM, Analytics.
"""

import logging
from data_manager import get_user_data, get_all_users
from bi import compute_team_kpi, weekly_report, nps_score

logger = logging.getLogger(__name__)

def get_user_dashboard(user_id):
    """
    Restituisce la dashboard personale dell’utente (progressi, badge, pv, step, avanzamento, ranking).
    """
    user = get_user_data(user_id)
    if not user:
        return "Utente non trovato."
    dashboard = (
        f"👤 {user['name']} ({user['city']}) — {user['level']}\n"
        f"PV Mese: {user['pv_mese']}\n"
        f"PV Team: {user['pv_team']}\n"
        f"Badge: {', '.join(user['badges']) if user['badges'] else 'Nessuno'}\n"
        f"Engagement: {user['engagement']} punti\n"
    )
    return dashboard

def get_leaderboard(top_n=10):
    """
    Restituisce la classifica top N (es. top 10) per PV Team o badge.
    """
    users = get_all_users()
    sorted_users = sorted(users, key=lambda u: u.get("pv_team", 0), reverse=True)
    leaderboard = "🏆 *Leaderboard Massimo AI*\n"
    for idx, u in enumerate(sorted_users[:top_n]):
        leaderboard += f"{idx+1}. {u['name']} — PV Team: {u['pv_team']} — Badge: {', '.join(u['badges'])}\n"
    return leaderboard

def get_admin_dashboard():
    """
    Dashboard per amministratori/leader: KPI, report, NPS, alert.
    """
    kpi = compute_team_kpi()
    report = weekly_report()
    nps = nps_score()
    dashboard = (
        f"{report}\n"
        f"NPS team: {nps:.1f}\n"
        f"Attivi: {kpi['active']}/{kpi['user_count']}\n"
        f"Churn: {kpi['churn']}\n"
        f"Director: {kpi['directors']}\n"
    )
    return dashboard

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(get_user_dashboard(1))
    print(get_leaderboard())
    print(get_admin_dashboard())
