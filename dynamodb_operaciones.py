#!/usr/bin/env python3
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'devops-tabla'

print("=== SCRIPT DYNAMODB OPERACIONES ===\n")

# 1. Crear tabla
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
    AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
    BillingMode='PAY_PER_REQUEST'
)
table.wait_until_exists()
print(f"Tabla '{table_name}' creada")

# 2. Insertar registro
table.put_item(Item={
    'id': '001',
    'nombre': 'Proyecto DevOps',
    'status': 'Activo'
})
print("Registro insertado")

# 3. Modificar registro
table.update_item(
    Key={'id': '001'},
    UpdateExpression="SET #s = :val",
    ExpressionAttributeNames={'#s': 'status'},
    ExpressionAttributeValues={':val': 'En progreso'}
)
print("Registro modificado (status actualizado)")

# 4. Eliminar registro
table.delete_item(Key={'id': '001'})
print("Registro eliminado")

print("\n=== OPERACIONES EN DYNAMODB FINALIZADAS ===")
