#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de automatización - Sección 4
Utiliza boto3 para:
- Listar instancias EC2
- Reporte de uso de CPU (últimas 24 horas)
- Listar buckets S3 y sus objetos
- Consultar grupos de Auto Scaling
"""

import boto3
from datetime import datetime, timedelta

# Crear clientes de boto3
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')
s3 = boto3.client('s3')
autoscaling = boto3.client('autoscaling')

print("=== REPORTE DE AUTOMATIZACIÓN AWS ===\n")

# 1. Listar todas las instancias EC2
print("1. INSTANCIAS EC2:")
response = ec2.describe_instances()
instances = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        inst_id = instance['InstanceId']
        inst_type = instance['InstanceType']
        state = instance['State']['Name']
        print(f"   • ID: {inst_id} | Tipo: {inst_type} | Estado: {state}")
        instances.append({'id': inst_id, 'state': state})

print("\n" + "="*50 + "\n")

# 2. Reporte de uso de CPU de instancias en ejecución (últimas 24 horas)
print("2. REPORTE DE CPU (últimas 24 horas) - Instancias en ejecución:")
end_time = datetime.utcnow()
start_time = end_time - timedelta(hours=24)

for inst in instances:
    if inst['state'] == 'running':
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': inst['id']}],
            StartTime=start_time,
            EndTime=end_time,
            Period=3600,          # 1 hora
            Statistics=['Average']
        )
        if response['Datapoints']:
            avg_cpu = sum(dp['Average'] for dp in response['Datapoints']) / len(response['Datapoints'])
            print(f"   • Instancia {inst['id']}: Promedio CPU = {avg_cpu:.2f}%")
        else:
            print(f"   • Instancia {inst['id']}: Sin datos de CPU disponibles")

print("\n" + "="*50 + "\n")

# 3. Listar buckets S3 y sus objetos
print("3. BUCKETS S3 Y OBJETOS:")
buckets = s3.list_buckets()['Buckets']
for bucket in buckets:
    bucket_name = bucket['Name']
    print(f"   • Bucket: {bucket_name}")
    try:
        objects = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                print(f"       - {obj['Key']} ({obj['Size']} bytes)")
        else:
            print("       (vacío)")
    except Exception as e:
        print(f"       Error al listar objetos: {e}")

print("\n" + "="*50 + "\n")

# 4. Grupos de Auto Scaling
print("4. GRUPOS DE AUTO SCALING:")
asg_response = autoscaling.describe_auto_scaling_groups()
for group in asg_response['AutoScalingGroups']:
    print(f"   • Grupo: {group['AutoScalingGroupName']}")
    print(f"       Min: {group['MinSize']} | Max: {group['MaxSize']} | Deseado: {group['DesiredCapacity']}")

print("\n=== FIN DEL REPORTE ===")
