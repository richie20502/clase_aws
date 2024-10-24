
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



