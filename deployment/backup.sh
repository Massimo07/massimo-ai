#!/bin/bash
DATE=$(date +"%Y%m%d_%H%M%S")
PGPASSWORD=superpass pg_dump -U massimo -h db massimoai > "/backup/db_backup_$DATE.sql"
echo "Backup creato in /backup/db_backup_$DATE.sql"
