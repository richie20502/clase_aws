# Proyecto de Ejemplo con Amazon S3

Este proyecto muestra cómo trabajar con Amazon S3 para almacenar y acceder a imágenes. A continuación se detallan los pasos para subir una imagen y hacer referencia a ella.

## Crear un Bucket de S3

1. Inicia sesión en la [Consola de administración de AWS](https://aws.amazon.com/console/).
2. Navega a **S3**
![Gráfico de Ejemplo](https://prueba-image.s3.us-east-1.amazonaws.com/Screenshot+2024-10-23+003814.png)
3.  y haz clic en **Crear bucket**.
![Gráfico de Ejemplo](https://prueba-image.s3.us-east-1.amazonaws.com/Screenshot+2024-10-23+003839.png)
4. Asigna un nombre único al bucket (por ejemplo, `prueba-image`) y selecciona una región.
![Gráfico de Ejemplo](https://prueba-image.s3.us-east-1.amazonaws.com/Screenshot+2024-10-23+003929.png)
5. Configura las opciones del bucket según tus necesidades y haz clic en **Crear bucket**.
![Gráfico de Ejemplo](https://prueba-image.s3.us-east-1.amazonaws.com/Screenshot+2024-10-23+010145.png)
6. Se genero el bucket 
![Gráfico de Ejemplo](https://prueba-image.s3.us-east-1.amazonaws.com/Screenshot+2024-10-23+010312.png)

7. Pestana de persmisos del bucket asignarle estos permisos

```bash 
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::prueba-image",
                "arn:aws:s3:::prueba-image/*"
            ]
        }
    ]
}
```
