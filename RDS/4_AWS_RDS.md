# AWS RDS (Relational Database Service)

## ¿Qué es RDS?
**Amazon RDS (Relational Database Service)** es un servicio administrado de **bases de datos relacionales** en la nube de AWS. RDS facilita la configuración, operación y escalado de bases de datos, permitiendo que los desarrolladores se enfoquen en sus aplicaciones sin preocuparse por la gestión de servidores y tareas administrativas como **respaldos, actualizaciones** o **recuperación de fallos**. 

---

## **Motores de Base de Datos Compatibles**
- **Amazon Aurora**: Optimizado para la nube y compatible con **MySQL** y **PostgreSQL**.
- **MySQL**: Base de datos popular de código abierto.
- **PostgreSQL**: Base avanzada con soporte para extensiones.
- **MariaDB**: Variante de MySQL con mejoras de rendimiento.
- **Oracle Database**: Con opciones de licencias de Oracle.
- **Microsoft SQL Server**: Ideal para aplicaciones empresariales de Microsoft.

---

## **Características Principales**
1. **Automatización de Backups**  
   - RDS realiza **respaldos automáticos diarios** y permite crear **snapshots** manuales.  
   - Posibilidad de restaurar a un momento específico con **point-in-time recovery**.

2. **Alta Disponibilidad con Multi-AZ**  
   - Réplicas en **múltiples zonas de disponibilidad** (AZs) para garantizar alta disponibilidad y resiliencia.

3. **Escalabilidad**  
   - **Escalamiento vertical:** Cambia el tamaño de la instancia sin interrupciones significativas.  
   - **Réplicas de lectura:** Distribuye la carga de trabajo aumentando el rendimiento de lectura.

4. **Seguridad Integrada**  
   - **Cifrado en reposo y en tránsito** mediante AWS KMS.  
   - Control de acceso detallado con **IAM** y reglas de **VPC** para aislamiento de red.

5. **Monitoreo y Optimización**  
   - Integración con **CloudWatch** para monitoreo en tiempo real.  
   - Recomendaciones automáticas de **Trusted Advisor** para mejorar rendimiento y reducir costos.

---

## **Casos de Uso Comunes**
- **Aplicaciones empresariales** que requieren alta disponibilidad y escalabilidad.
- **Sistemas de gestión de contenido (CMS)** que utilizan bases de datos relacionales.
- **E-commerce** que necesita manejar grandes volúmenes de transacciones.
- **Análisis de datos en tiempo real** utilizando motores como Aurora.

---

## **Tipos de Almacenamiento en RDS**
1. **Almacenamiento General (SSD GP3/GP2):**  
   - Recomendado para cargas de trabajo estándar.

2. **Almacenamiento Provisional (IOPS Provisionadas):**  
   - Ideal para aplicaciones que requieren baja latencia y alto rendimiento de E/S.

3. **Almacenamiento Magnético:**  
   - Opción más económica, adecuada para cargas ligeras o no críticas.

---

## **Modelos de Precios**
- **On-Demand:** Paga solo por el tiempo de uso sin compromisos.  
- **Reserved Instances:** Ahorra hasta un 75% con reservas de 1 o 3 años.  
- **Free Tier:** Uso gratuito limitado con MySQL, PostgreSQL y SQL Server durante el primer año.

---

## **Más Información**
- [Página Oficial de AWS RDS](https://aws.amazon.com/rds/)
- [Precios de RDS](https://aws.amazon.com/rds/pricing/)
- [Documentación Oficial](https://docs.aws.amazon.com/rds/)

---
