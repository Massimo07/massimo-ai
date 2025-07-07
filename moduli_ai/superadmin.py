"""
Modulo: superadmin.py
Strumenti avanzati per super-admin: esporta log, visualizza ogni utente, audit, statistiche avanzate, reset e upgrade live.
"""

import data_manager
import log_audit

def export_all_logs(filename="all_logs.txt"):
    logs = log_audit.get_audit_log()
    with open(filename, "w") as f:
        for entry in logs:
            f.write(str(entry) + "\n")
    return filename

def audit_user(user_id):
    user = data_manager.get_user_data(user_id)
    logs = log_audit.get_user_log(user_id)
    return {"user": user, "logs": logs}

def system_reset(confirm=False):
    if confirm:
        # Esegui pulizia log, reset dati demo
        open("all_logs.txt", "w").close()
        print("Reset completo di sistema.")
    else:
        print("Attenzione: passare confirm=True per eseguire reset!")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(export_all_logs())
    print(audit_user(1))
    system_reset(confirm=True)
