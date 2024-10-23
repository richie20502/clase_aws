
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

--------------------------------------------------------------------------------------------------------------------------------------

# AWS RDS (Relational Database Service)

## ¿Qué es RDS?
**Amazon RDS (Relational Database Service)** es un servicio administrado de bases de datos relacionales en la nube de AWS. Simplifica la configuración, operación y escalado de bases de datos, eliminando tareas complejas como la administración de servidores, actualizaciones de software, respaldos y recuperación. 

Con **RDS**, los usuarios pueden enfocarse en optimizar sus aplicaciones mientras AWS gestiona la infraestructura subyacente.

---

## **¿Cómo funciona AWS RDS?**
RDS permite implementar bases de datos en la nube en cuestión de minutos, ofreciendo:
- **Automatización** de tareas administrativas como actualizaciones y copias de seguridad.
- **Alta disponibilidad** con réplicas multi-zona (Multi-AZ).
- **Escalabilidad** vertical y horizontal para gestionar el crecimiento de los datos.
- **Seguridad** integrada con cifrado en reposo y en tránsito, y control de acceso con **IAM**.

---

## **Motores de Base de Datos Soportados**
- **Amazon Aurora**: Una base de datos optimizada para la nube, compatible con MySQL y PostgreSQL.
- **MySQL**: Soporte completo para bases de datos relacionales de código abierto.
- **PostgreSQL**: Ofrece características avanzadas y soporte de extensiones.
- **MariaDB**: Una variante de MySQL con mejoras de rendimiento.
- **Oracle Database**: Con licencias opcionales de Oracle.
- **Microsoft SQL Server**: Compatible con aplicaciones Windows.

---

## **Características Principales de RDS**
1. **Automatización de Backups**  
   - RDS realiza **respaldos automáticos diarios** y permite crear **snapshots** manuales.

2. **Alta Disponibilidad con Multi-AZ**  
   - Réplicas en múltiples zonas de disponibilidad garantizan la **resiliencia ante fallos**.

3. **Escalabilidad**  
   - **Escalamiento vertical:** Aumenta la capacidad del servidor de forma sencilla.  
   - **Réplicas de lectura:** Escala horizontalmente distribuyendo la carga de consultas.

4. **Seguridad**  
   - **Cifrado:** Datos cifrados en reposo y en tránsito mediante AWS KMS.  
   - **Acceso controlado:** Gestión de usuarios y roles con IAM.

---

## **Casos de Uso**
- **Aplicaciones empresariales** con necesidades de bases de datos escalables.
- **Sistemas ERP y CRM** que requieren alta disponibilidad.
- **Aplicaciones web** que usan bases de datos relacionales para gestionar usuarios y contenido.
- **Analítica en tiempo real** con bases optimizadas como **Aurora**.

---

## **Precios**
El costo de RDS depende del motor elegido, el tamaño de la instancia, el almacenamiento utilizado y el tráfico de red.  
Consulta los precios en: [Precios de AWS RDS](https://aws.amazon.com/rds/pricing/)

---

## **Más Información**
- [Documentación Oficial de RDS](https://docs.aws.amazon.com/rds/)
- [Amazon Aurora](https://aws.amazon.com/rds/aurora/)
- [Guía de RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/)

---



