import json

def lambda_handler(event, context):
    temperature = event['temperature']
    vibration = event['vibration']
    humidity = event['humidity']
    # Simulação de processamento
    maintenance_required = temperature > 50 or vibration > 1 or humidity > 60
    
    result = {
        "maintenance_required": maintenance_required,
        "details": event
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
