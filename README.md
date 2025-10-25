# 🚀 DÍA 2: Microservicio Backend Auth

## 🎯 Objetivo General

Construir un **microservicio de autenticación** (`auth-service`) completamente independiente. Este servicio debe ser capaz de manejar:
1.  Registro de usuarios, login y gestión de **tokens JWT**.
2.  Correr en su propio **contenedor Docker**.
3.  Conectarse a **PostgreSQL** (persistencias) y **Redis** (cache/sesiones).

## 🧠 Conceptos Clave a Aplicar

* **Autenticación basada en JWT** (JSON Web Tokens).
* Estructura de un servicio Django aislado.
* Configuración de **variables de entorno** y dependencias.
* **Cacheo y sesiones con Redis**.
* Comunicación segura entre servicios vía API.

## 🛠️ Estructura del Proyecto

El microservicio se encuentra dentro de la carpeta `auth-service/`.

### 📄 Pasos Esenciales

1.  **Estructura Base:** Crear el proyecto Django y la app `users` dentro de `auth-service/`.
2.  **Dockerfile:** Definir el proceso de construcción del contenedor, incluyendo la imagen base (`python:3.11`), la instalación de dependencias y el comando `gunicorn` para arrancar el servicio en el **puerto 8000**.
3.  **Docker Compose:** Extender `docker-compose.yml` en la raíz del proyecto para añadir el servicio `auth`.Debe establecer las variables de entorno de la base de datos y Redis, y declarar `depends_on: [postgres, redis]`.
4.  **Dependencias (requirements.txt):** Instalar Django, Django REST Framework, `djangorestframework-simplejwt`, `psycopg2-binary`, `redis`, y `django-cors-headers`.
5.  **Configuración (`settings.py`):**
    * Añadir `rest_framework`, `corsheaders`, y la app `users` a `INSTALLED_APPS`.
    * Configurar `DATABASES` y `CACHES` (usando Redis) con variables de entorno.
    * Definir `REST_FRAMEWORK` para usar `JWTAuthentication`.
6.  **Modelo de Usuario:** Crear un modelo de usuario personalizado (`users/models.py`) que herede de `AbstractBaseUser` y use el `email` como `USERNAME_FIELD`. Registrar en `settings.py` con `AUTH_USER_MODEL = 'users.User'`.
7.  **Endpoints JWT:** Configurar las rutas para **Login**, **Token Refresh** y el endpoint para **Registro** (`/api/register/`).

### 🧪 Pruebas y Endpoints (Postman)

Se deben probar los siguientes endpoints para verificar la funcionalidad:

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| `POST` | `/api/register/` | Crea un nuevo usuario. |
| `POST` | `/api/token/` | Genera `access` y `refresh` tokens al loguearse. |
| `POST` | `/api/token/refresh/` | Renueva el token de acceso. |

🎯 ### Entrar a Admin:
URL: http://127.0.0.1:8000/admin/
email: matias@example.com
contraseña: mat123

**Verificación de Conexión:**
Se puede verificar la conexión a la base de datos y Redis ejecutando un *shell* dentro del contenedor:
```bash
docker exec -it auth_service python manage.py shell