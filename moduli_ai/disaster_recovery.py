"""
Modulo: disaster_recovery.py
Backup automatico DB, knowledge, configurazione. Script di ripristino semplice, reportistica backup.
Pronto per cron, server, cloud, esportazione automatica (anche su S3).
"""

import os
import shutil
import logging
from datetime import datetime

logger = logging.getLogger("massimoai.dr")

BACKUP_DIR = "backups/"

def backup_all():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    files_to_backup = ["massimo_ai.db", "knowledge_base.json", ".env"]
    backup_paths = []
    for fname in files_to_backup:
        if os.path.exists(fname):
            bname = f"{BACKUP_DIR}{fname}_{ts}"
            shutil.copy(fname, bname)
            backup_paths.append(bname)
            logger.info(f"Backup: {fname} → {bname}")
    return backup_paths

def list_backups():
    if not os.path.exists(BACKUP_DIR):
        return []
    return os.listdir(BACKUP_DIR)

def restore_backup(filename):
    """Ripristina un file backup (ATTENZIONE: sovrascrive i dati attuali!)."""
    if not os.path.exists(f"{BACKUP_DIR}{filename}"):
        raise FileNotFoundError("Backup non trovato.")
    orig_name = filename.split("_")[0]
    shutil.copy(f"{BACKUP_DIR}{filename}", orig_name)
    logger.info(f"Ripristino: {filename} → {orig_name}")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    backup_all()
    print(list_backups())
