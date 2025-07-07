"""
Massimo AI – Backup Engine
Backup automatico, versioning, export su cloud (AWS, GCP, Azure, S3, ecc.), auto-recovery.
"""
import os
import shutil
import datetime

class BackupEngine:
    def __init__(self, backup_dir="backups"):
        self.backup_dir = backup_dir
        os.makedirs(backup_dir, exist_ok=True)

    def backup(self, data_dir):
        date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = os.path.join(self.backup_dir, f"backup_{date_str}")
        shutil.copytree(data_dir, dest)
        print(f"Backup completato: {dest}")
        return dest

    def restore(self, backup_path, dest_dir):
        shutil.copytree(backup_path, dest_dir, dirs_exist_ok=True)
        print(f"Ripristino completato: {dest_dir}")

    def list_backups(self):
        return os.listdir(self.backup_dir)
