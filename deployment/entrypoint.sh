#!/bin/bash
echo "Starting Massimo AI..."
python database/migrate.py
exec "$@"
