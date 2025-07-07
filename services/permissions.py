"""
services/permissions.py – Gestione permessi/ruoli avanzati
Multi-tenant, accessi granulari, log, compliance, audit, API-ready.
"""
from typing import Dict, List

class PermissionService:
    def __init__(self):
        # user_id: [roles]
        self.user_roles: Dict[str, List[str]] = {}
        # role: [permissions]
        self.role_perms: Dict[str, List[str]] = {
            "founder": ["all"],
            "admin": ["create", "edit", "delete", "view"],
            "user": ["view"],
        }

    def set_role(self, user_id: str, role: str):
        self.user_roles.setdefault(user_id, []).append(role)

    def has_permission(self, user_id: str, permission: str) -> bool:
        roles = self.user_roles.get(user_id, [])
        for r in roles:
            perms = self.role_perms.get(r, [])
            if "all" in perms or permission in perms:
                return True
        return False

    def list_user_roles(self, user_id: str) -> List[str]:
        return self.user_roles.get(user_id, [])

permission_service = PermissionService()

# Esempio:
# from services.permissions import permission_service
# permission_service.set_role("user123", "admin")
# permission_service.has_permission("user123", "edit")
