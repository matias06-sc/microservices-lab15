# 🚀 DÍA 2: Microservicio Backend Auth

## 🎯 Objetivo General

[cite_start]Construir un **microservicio de autenticación** (`auth-service`) completamente independiente[cite: 388]. Este servicio debe ser capaz de manejar:
1.  [cite_start]Registro de usuarios, login y gestión de **tokens JWT**[cite: 388].
2.  [cite_start]Correr en su propio **contenedor Docker**[cite: 388].
3.  [cite_start]Conectarse a **PostgreSQL** (persistencias) y **Redis** (cache/sesiones)[cite: 388].

## 🧠 Conceptos Clave a Aplicar

* [cite_start]**Autenticación basada en JWT** (JSON Web Tokens)[cite: 390].
* [cite_start]Estructura de un servicio Django aislado[cite: 391].
* [cite_start]Configuración de **variables de entorno** y dependencias[cite: 392].
* [cite_start]**Cacheo y sesiones con Redis**[cite: 393].
* [cite_start]Comunicación segura entre servicios vía API[cite: 394].

## 🛠️ Estructura del Proyecto

El microservicio se encuentra dentro de la carpeta `auth-service/`.

### 📄 Pasos Esenciales

1.  [cite_start]**Estructura Base:** Crear el proyecto Django y la app `users` dentro de `auth-service/`[cite: 400, 401, 402, 403].
2.  [cite_start]**Dockerfile:** Definir el proceso de construcción del contenedor, incluyendo la imagen base (`python:3.11`), la instalación de dependencias y el comando `gunicorn` para arrancar el servicio en el **puerto 8000**[cite: 405, 406, 407, 408, 409, 410, 428].
3.  **Docker Compose:** Extender `docker-compose.yml` en la raíz del proyecto para añadir el servicio `auth`. [cite_start]Debe establecer las variables de entorno de la base de datos y Redis, y declarar `depends_on: [postgres, redis]`[cite: 411, 412, 413, 414, 415, 416, 424, 427, 418, 420, 421, 422, 423].
4.  [cite_start]**Dependencias (requirements.txt):** Instalar Django, Django REST Framework, `djangorestframework-simplejwt`, `psycopg2-binary`, `redis`, y `django-cors-headers`[cite: 429, 430, 431, 432, 433, 434, 435].
5.  **Configuración (`settings.py`):**
    * [cite_start]Añadir `rest_framework`, `corsheaders`, y la app `users` a `INSTALLED_APPS`[cite: 437].
    * [cite_start]Configurar `DATABASES` y `CACHES` (usando Redis) con variables de entorno[cite: 438, 439].
    * [cite_start]Definir `REST_FRAMEWORK` para usar `JWTAuthentication`[cite: 442].
6.  [cite_start]**Modelo de Usuario:** Crear un modelo de usuario personalizado (`users/models.py`) que herede de `AbstractBaseUser` y use el `email` como `USERNAME_FIELD`[cite: 443, 455, 456, 458]. Registrar en `settings.py` con `AUTH_USER_MODEL = 'users.User'`[cite: 462].
7.  [cite_start]**Endpoints JWT:** Configurar las rutas para **Login**, **Token Refresh** y el endpoint para **Registro** (`/api/register/`)[cite: 462].

### 🧪 Pruebas y Endpoints (Postman)

[cite_start]Se deben probar los siguientes endpoints para verificar la funcionalidad[cite: 463]:

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| `POST` | `/api/register/` | Crea un nuevo usuario. |
| `POST` | `/api/token/` | Genera `access` y `refresh` tokens al loguearse. |
| `POST` | `/api/token/refresh/` | Renueva el token de acceso. |

**Verificación de Conexión:**
[cite_start]Se puede verificar la conexión a la base de datos y Redis ejecutando un *shell* dentro del contenedor[cite: 463]:
```bash
docker exec -it auth_service python manage.py shell