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
- [Calculadora Ec2](https://calculator.aws/#/addService)

-----------------------------------------------------------------------------------------
