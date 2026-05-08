#!/bin/bash
# Script de gestión de usuarios y permisos - Sección 3

echo "=== Creando usuario devops_user ==="
sudo useradd -m -s /bin/bash devops_user

echo "=== Asignando permisos sobre el entorno ==="
sudo chown -R devops_user:devops_user ~/environment

echo "=== Agregando usuario al grupo docker (opcional pero recomendado) ==="
sudo usermod -aG docker devops_user

echo "=== Restaurando permisos para ec2-user (IMPORTANTE) ==="
sudo chown -R ec2-user:ec2-user ~/environment

echo "=== Script de usuarios completado ==="
