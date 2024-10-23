import boto3

# Inicializa el cliente de IAM
iam_client = boto3.client('iam')

# Obtiene información del usuario actual
user = iam_client.get_user()
user_name = user['User']['UserName']

# Muestra el nombre del usuario
print(f"Usuario actual: {user_name}")

# Obtiene las políticas adjuntas al usuario
policies = iam_client.list_attached_user_policies(UserName=user_name)

# Muestra las políticas
print(f"Políticas adjuntas al usuario {user_name}:")
for policy in policies['AttachedPolicies']:
    print(f"- {policy['PolicyName']} (ARN: {policy['PolicyArn']})")
