#!/bin/bash
# Script de instalación de dependencias - Sección 3

echo "=== Instalando dependencias ==="
sudo yum update -y
sudo yum install -y python3-pip

echo "=== Instalando boto3 ==="
pip3 install boto3 --user

echo "=== Instalación completada ==="
