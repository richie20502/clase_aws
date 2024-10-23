import boto3

# Inicializa el cliente de Bedrock
bedrock_client = boto3.client('bedrock', region_name='us-east-1')

# Llama a la función para listar los modelos
try:
    response = bedrock_client.list_foundation_models()

    # Muestra la lista de modelos
    models = response['modelSummaries']
    for model in models:
        print(f"Modelo ID: {model['modelId']}")
        
except Exception as e:
    print(f"Ocurrió un error: {e}")
