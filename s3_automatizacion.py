#!/usr/bin/env python3
import boto3
import os

s3 = boto3.client('s3')
bucket_name = 'devops-bucket-545571807071'

print("=== SCRIPT S3 AUTOMATIZACIÓN ===\n")

# Crear archivo de prueba local
with open('archivo_prueba.txt', 'w') as f:
    f.write("Este es un archivo de prueba para el proyecto DevOps\n")
print("Archivo de prueba creado localmente")

# Subir archivo al bucket en carpeta pruebas/
s3.upload_file('archivo_prueba.txt', bucket_name, 'pruebas/archivo_prueba.txt')
print(f"Archivo subido a s3://{bucket_name}/pruebas/archivo_prueba.txt")

# Listar todos los objetos del bucket
print("\nObjetos en el bucket:")
response = s3.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        print(f"   • {obj['Key']}  |  {obj['Size']} bytes  |  {obj['LastModified']}")
else:
    print("   (El bucket está vacío)")
