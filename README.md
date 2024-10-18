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

### 2. Crear el directorio de la aplicación Flask
```bash
sudo mkdir -p /opt/flask_app
sudo chown ec2-user:ec2-user /opt/flask_app
cd /opt/flask_app
