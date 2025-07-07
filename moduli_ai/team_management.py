"""
Modulo: team_management.py
Gestione struttura del team: membri, livelli, avanzamento, progressi, performance individuali e di gruppo, visualizzazione gerarchia.
Pronto per dashboard, automazioni, leaderboard.
"""

import logging
from data_manager import get_user_data, get_all_users, update_user_data

logger = logging.getLogger(__name__)

def get_team(user_id):
    """Restituisce i membri del team diretti di un utente."""
    users = get_all_users()
    return [u for u in users if u.get("sponsor") == user_id]

def team_progress(user_id):
    """Calcola progressi e performance del team di un utente."""
    team = get_team(user_id)
    total_pv = sum(u.get("pv_mese", 0) for u in team)
    directors = sum(1 for u in team if u.get("level") == "Director")
    return {"members": len(team), "total_pv": total_pv, "directors": directors}

def upgrade_team_member(user_id, new_level):
    """Promuove un membro del team a un nuovo livello."""
    update_user_data(user_id, level=new_level)
    logger.info(f"Team member {user_id} promosso a {new_level}")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(get_team(12345))
    print(team_progress(12345))
    upgrade_team_member(67890, "Director")
from data_manager import get_team_members, get_progress

def get_team_overview(team_leader_id):
    members = get_team_members(team_leader_id)
    overview = []
    for member in members:
        progress = get_progress(member['user_id'])
        overview.append({'member': member, 'progress': progress})
    return overview
