# AWS Secrets Manager: Guía Rápida

## 🔐 ¿Qué es AWS Secrets Manager?

**AWS Secrets Manager** es un servicio de almacenamiento de secretos que ayuda a proteger el acceso a tus aplicaciones, servicios y recursos de TI. En lugar de escribir "a fuego" (hardcoding) tus credenciales en el código fuente, las guardas en AWS y las consultas programáticamente.



### 🌟 Funcionalidades Clave

* **Gestión Centralizada:** Almacena credenciales de bases de datos, claves de API, tokens de OAuth y más en un solo lugar.
* **Rotación Automática:** Puede cambiar automáticamente las contraseñas (por ejemplo, de RDS o Redshift) sin intervención humana y sin tiempo de inactividad.
* **Seguridad Robusta:** Utiliza **AWS KMS** (Key Management Service) para cifrar los secretos en reposo.
* **Control de Acceso:** Se integra con **IAM** para definir exactamente qué usuarios o roles de Lambda/EC2 pueden leer un secreto específico.

---

## 🚀 ¿Por qué usarlo en lugar de variables de entorno?

| Característica | Variables de Entorno (.env) | AWS Secrets Manager |
| :--- | :--- | :--- |
| **Seguridad** | Expuestas en texto plano en el server. | Cifradas con KMS. |
| **Rotación** | Manual y propensa a errores. | Automática y programable. |
| **Auditoría** | Difícil de rastrear quién accedió. | Integrado con CloudTrail. |
| **Escalabilidad** | Difícil de gestionar en microservicios. | Acceso centralizado via SDK/CLI. |

---

## 🛠️ Cómo se usa (Ejemplo conceptual)

En lugar de tener esto en tu código:
`const db_pass = "admin12345"; // ❌ MALA PRÁCTICA`

El flujo correcto es:
1. La aplicación solicita el secreto al **Secrets Manager API**.
2. El servicio descifra el valor y lo entrega de forma segura.
3. La aplicación usa la credencial en memoria.

### Ejemplo rápido con AWS CLI
```bash
aws secretsmanager get-secret-value --secret-id MiApp/Database/Password