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





# AWS EC2 (Elastic Compute Cloud)

## ¿Qué es EC2?
**Amazon EC2 (Elastic Compute Cloud)** es un servicio de cómputo en la nube que proporciona **capacidad de procesamiento escalable**. Permite lanzar servidores virtuales (llamados **instancias**) para ejecutar aplicaciones sin necesidad de gestionar infraestructura física. Con EC2, solo pagas por el tiempo en que tus instancias están en uso, y puedes ajustar la capacidad en función de tus necesidades.

---

## **¿Cómo funciona EC2?**
- Las **instancias EC2** son servidores virtuales que se ejecutan en la infraestructura de AWS.
- Puedes elegir entre diferentes tipos de instancias, optimizados para tareas específicas, como procesamiento general, computación intensiva, o memoria optimizada.
- AWS te permite lanzar instancias bajo diferentes modelos de pago: **On-Demand**, **Reserved Instances**, **Savings Plans** o **Spot Instances**.

---

## **Tipos de instancias EC2**

| **Familia**          | **Descripción**                                                  | **Usos Comunes**                                  |
|----------------------|------------------------------------------------------------------|--------------------------------------------------|
| **General Purpose**  | Balance entre procesamiento, memoria y redes.                   | Aplicaciones web, servidores de desarrollo.      |
| **Compute Optimized**| Optimizadas para tareas que requieren gran poder de CPU.         | Análisis intensivo, procesamiento de datos.      |
| **Memory Optimized** | Diseñadas para cargas de trabajo con gran consumo de memoria.    | Bases de datos en memoria, análisis en tiempo real. |
| **Storage Optimized**| Ofrecen alto rendimiento en operaciones de E/S de almacenamiento.| Almacenamiento de datos masivos, bases NoSQL.    |
| **Accelerated Computing**| Utilizan GPU o FPGA para tareas especializadas.              | Machine Learning, procesamiento gráfico.         |

---

### **Ejemplos de Tipos de Instancias**

1. **General Purpose (t2, t3, t4g)**
   - Balance entre CPU, memoria y almacenamiento.
   - Ideal para servidores web, entornos de pruebas y aplicaciones de baja latencia.
   - **Ejemplo:** `t3.micro` (usado en el nivel gratuito de AWS).

2. **Compute Optimized (c5, c6g)**
   - Optimizadas para alto rendimiento de CPU.
   - Usadas para simulaciones científicas, videojuegos y servidores de alta carga.
   - **Ejemplo:** `c5.xlarge`.

3. **Memory Optimized (r5, r6g)**
   - Ofrecen más memoria por núcleo que otras familias.
   - Perfectas para bases de datos grandes y análisis en tiempo real.
   - **Ejemplo:** `r5.large`.

4. **Storage Optimized (i3, i4g, d2)**
   - Diseñadas para aplicaciones que requieren operaciones rápidas de lectura/escritura.
   - Comúnmente usadas en bases de datos NoSQL o almacenamiento distribuido.
   - **Ejemplo:** `i3.4xlarge`.

5. **Accelerated Computing (p4, g5, f1)**
   - Equipadas con GPU o FPGA para cargas de trabajo especializadas.
   - Utilizadas en inteligencia artificial, aprendizaje profundo y renderización.
   - **Ejemplo:** `p4d.24xlarge`.

---

## **Modelos de Compra**
- **On-Demand:** Paga por hora/segundo sin compromisos a largo plazo.  
- **Reserved Instances:** Ahorros significativos al reservar instancias por 1 o 3 años.  
- **Savings Plans:** Compromiso de gasto para obtener descuentos en EC2 y otros servicios.  
- **Spot Instances:** Adquiere capacidad no utilizada a menor costo, pero las instancias pueden ser interrumpidas.

---

## **Casos de Uso Comunes**
- **Aplicaciones web escalables** que necesitan adaptarse a la demanda del tráfico.
- **Bases de datos** y almacenamiento distribuido.
- **Análisis intensivo de datos** con procesamiento paralelo.
- **Entrenamiento de modelos de Machine Learning** con instancias aceleradas por GPU.

---

## **Más Información**
- [Documentación Oficial de EC2](https://docs.aws.amazon.com/ec2)
- [Precios de EC2](https://aws.amazon.com/ec2/pricing/)
- [Tipos de Instancias EC2](https://aws.amazon.com/ec2/instance-types/)

-----------------------------------------------------------------------------------------

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



