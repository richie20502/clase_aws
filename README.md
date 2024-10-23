# Introducción a AWS (Amazon Web Services)

## ¿Qué es AWS?
**Amazon Web Services (AWS)** es una plataforma de **servicios en la nube** que ofrece soluciones tecnológicas bajo demanda. Permite a empresas y desarrolladores acceder a recursos de almacenamiento, procesamiento, bases de datos, redes y más, sin necesidad de gestionar infraestructura física. Con AWS, pagas solo por los recursos que consumes, lo que facilita la escalabilidad y la optimización de costos.



## ¿Cómo trabaja AWS?

AWS se basa en el concepto de **infraestructura como servicio (IaaS)**, **plataforma como servicio (PaaS)** y **software como servicio (SaaS)**. A continuación se explica su funcionamiento básico:

1. **Servicios Globales y Regiones**  
   - AWS está dividido en **regiones geográficas** que contienen varias **zonas de disponibilidad** (data centers).  
   - Puedes desplegar tus aplicaciones en múltiples regiones para mejorar la latencia y la resiliencia.

2. **Servicios Principales de AWS**  
   - **Cómputo:** EC2, Lambda (funciones sin servidor), ECS (contenedores).  
   - **Almacenamiento:** S3 (objetos), EBS (volúmenes), Glacier (archivado).  
   - **Bases de Datos:** RDS (relacional), DynamoDB (NoSQL), Redshift (analítica).  
   - **Redes:** VPC (redes privadas), CloudFront (CDN), Route 53 (DNS).  
   - **Seguridad:** IAM (gestión de identidades), CloudTrail (auditoría), GuardDuty (detección de amenazas).

3. **Modelo de Pago por Uso**  
   - Con AWS, solo pagas por los recursos que usas, sin contratos a largo plazo.
   - Algunos servicios ofrecen niveles **gratuitos** para que puedas experimentar con la plataforma sin costo.

4. **Automatización y Escalabilidad**  
   - AWS permite **automatizar** la creación y gestión de recursos con herramientas como **CloudFormation**.
   - Los servicios como **Auto Scaling** garantizan que las aplicaciones se ajusten automáticamente al tráfico y demanda.


## **Beneficios de AWS**
- **Escalabilidad:** Agrega recursos automáticamente según la demanda.
- **Alta disponibilidad:** Despliegue en múltiples regiones y zonas de disponibilidad para asegurar continuidad.
- **Seguridad:** Cumple con estándares internacionales de seguridad y privacidad.
- **Ecosistema amplio:** Compatible con múltiples tecnologías y lenguajes de programación.


## **Más información**
- [Página oficial de AWS](https://aws.amazon.com/)
- [Documentación de AWS](https://docs.aws.amazon.com/)
- [AWS Pricing Calculator](https://calculator.aws/#/)

---


# AWS IAM (Identity and Access Management)

**IAM** es un servicio de AWS que permite gestionar el acceso seguro a los recursos de la nube. Con IAM puedes crear usuarios, roles y políticas para definir qué acciones pueden realizar en la cuenta y qué recursos pueden acceder.

---

## **Conceptos clave**

### 1. Usuarios
- Representan personas o aplicaciones que necesitan acceso a los servicios.
- Pueden tener **contraseñas** o **access keys** para autenticarse en AWS.

### 2. Grupos
- Colección de usuarios que comparten las mismas políticas de permisos.
- Facilitan la administración centralizada de permisos para varios usuarios.

### 3. Roles
- Permiten asignar permisos a servicios de AWS, como EC2 o Lambda, sin usar credenciales permanentes.
- Ejemplo: Lambda puede asumir un rol para acceder a un bucket S3.

### 4. Políticas
- Documentos en formato **JSON** que definen las acciones permitidas o denegadas.
- Se pueden asociar a **usuarios, grupos o roles**.

## **Documentación y Recursos Útiles de AWS IAM**

1. **Documentación oficial de IAM**  
   [https://docs.aws.amazon.com/IAM](https://docs.aws.amazon.com/IAM)  
   _Página principal con toda la documentación oficial sobre IAM: guías, ejemplos y referencias API._

2. **Guía para comenzar con IAM**  
   [https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)  
   _Instrucciones para los primeros pasos con IAM: crear usuarios, roles y políticas._

3. **Políticas de IAM: Guía y ejemplos**  
   [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)  
   _Aprende a crear políticas y entiende cómo funcionan los permisos._

4. **Roles en IAM**  
   [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)  
   _Cómo usar roles para delegar permisos a servicios de AWS o usuarios externos._

5. **Mejores prácticas de seguridad con IAM**  
   [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)  
   _Recomendaciones para mantener tu cuenta segura mediante configuraciones adecuadas de IAM._


  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Configuración de Aplicación Flask en Amazon Linux con Nginx y Gunicorn

Este documento describe los pasos necesarios para configurar una aplicación Flask en una instancia de Amazon Linux utilizando Nginx como servidor web y Gunicorn como servidor WSGI.

## Prerrequisitos
- descarga mobaxTerm
- Una instancia de Amazon EC2 corriendo Amazon Linux.
- Acceso SSH a la instancia.
- Permisos para modificar las configuraciones del sistema.

## Instalación y Configuración

### 1. Permitir tráfico SSH y HTTP

Asegúrate de que tu grupo de seguridad permite el tráfico SSH y HTTP desde Internet.

### 2. Instalar Nginx

Ejecuta los siguientes comandos para instalar Nginx:

```bash
sudo dnf install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
```

### 3. Crear el directorio de la aplicación Flask
Crea el directorio para tu aplicación y establece los permisos adecuados:
```bash
sudo mkdir -p /opt/flask_app
sudo chown ec2-user:ec2-user /opt/flask_app
cd /opt/flask_app
```

### 4. Instalar Python y PIP
Instala Python 3 y pip:
```bash
sudo dnf install python3-pip -y
```

### 5. Instalar Flask y dependencias
Instala Flask y otras dependencias necesarias:
```bash
sudo pip3 install Flask gunicorn flask-restful flask-swagger-ui
```

### 6. Crear el archivo app.py
Crea el archivo app.py con el siguiente contenido:
```bash
vi app.py
```

```bash
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask on Amazon Linux with Nginx and Gunicorn!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

### 7. Ejecutar la aplicación Flask

Para probar la aplicación, ejecuta:

```bash
python3 app.py

```

### 8. Configurar Gunicorn como servicio
Determina la ruta de Gunicorn:
```bash
which gunicorn
```
Luego, crea el archivo de servicio para Gunicorn:

```bash
sudo vi /etc/systemd/system/flask_app.service
```

Agrega el siguiente contenido:
```bash
[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/opt/flask_app
ExecStart=/usr/local/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
```

### 9. Recargar el daemon de systemd y empezar el servicio
Ejecuta los siguientes comandos:
```bash
sudo systemctl daemon-reload
sudo systemctl start flask_app
sudo systemctl status flask_app
```

### 10. Configurar Nginx
Edita el archivo de configuración de Nginx:
```bash
sudo vi /etc/nginx/nginx.conf
```

Agrega el bloque server dentro de http:
```bash
server {
    listen 80;
    server_name 54.224.134.84;  # Reemplaza con tu dirección IPv4 public

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

```

### 11. Probar la configuración de Nginx
Verifica que no haya errores de sintaxis en la configuración de Nginx:
```bash
sudo nginx -t
```

### 12. Reiniciar Nginx
Si no hay errores, reinicia Nginx:

```bash
sudo systemctl restart nginx
```




