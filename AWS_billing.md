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
