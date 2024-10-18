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
