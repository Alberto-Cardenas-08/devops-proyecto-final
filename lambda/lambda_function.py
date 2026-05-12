import json
import random

def lambda_handler(event, context):
    mensajes = [
        "¡Bienvenido al proyecto DevOps en AWS!",
        "Microservicio desplegado con éxito mediante CI/CD",
        "Automatización y monitoreo completados",
        "Práctica real de Serverless Architecture",
        "Soluciones Tecnológicas del Futuro - Proyecto final"
    ]
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "mensaje": random.choice(mensajes),
            "servicio": "microservicio-devops"
        })
    }
