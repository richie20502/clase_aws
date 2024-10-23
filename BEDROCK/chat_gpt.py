import boto3
import json
import time  # Importa el módulo time

# Inicializa el cliente de Amazon Bedrock
client = boto3.client('bedrock-runtime', region_name='us-east-1')

def generar_respuesta(prompt):
    retries = 5  # Número de reintentos
    for attempt in range(retries):
        try:
            # Cuerpo de la solicitud
            body = {
                "inputText": prompt,  # El texto de entrada que el usuario proporciona
                "textGenerationConfig": {
                    "maxTokenCount": 3072,  # Ajustado al límite permitido
                    "stopSequences": [],
                    "temperature": 0,
                    "topP": 1
                }
            }

            # Invoca el modelo fundacional de Amazon Bedrock
            response = client.invoke_model(
                modelId='amazon.titan-text-premier-v1:0',  # Cambia según el modelo que uses
                contentType='application/json',  # Tipo de contenido correcto
                body=json.dumps(body)  # Convierte el cuerpo a JSON
            )

            # Procesa la respuesta
            result = response['body'].read().decode('utf-8')
            return json.loads(result)  # Decodifica la respuesta JSON

        except client.exceptions.ThrottlingException:
            print("Demasiadas solicitudes. Esperando antes de intentar nuevamente...")
            time.sleep(2 ** attempt)  # Exponencial: espera 1, 2, 4, 8... segundos
        except Exception as e:
            print(f"Error: {e}")
            return "Ocurrió un error al procesar tu solicitud."

# Bucle de interacción con el chatbot
if __name__ == "__main__":
    print("Chat GPT iniciado. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ['salir', 'exit']:
            print("Adiós!")
            break
        respuesta = generar_respuesta(user_input)
        print(f"Chat GPT: {respuesta}")
