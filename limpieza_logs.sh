#!/bin/bash
# Script de limpieza de logs - Sección 3

echo "=== Limpiando logs antiguos ==="
find ~/environment -name "*.log" -type f -mtime +7 -delete
find /var/log -name "*.log" -type f -mtime +7 -delete 2>/dev/null || true

echo "=== Limpieza de logs completada el $(date) ===" >> ~/environment/limpieza_logs.log
