# 🧱 Día 3 — Backend: Blog Service

Microservicio independiente desarrollado con **Django**, **MySQL**, **Redis** y **Docker**.  
Forma parte del proyecto de microservicios (Días 1–3).

---

## 🚀 Características principales

- **Framework:** Django 5 + Django REST Framework  
- **Base de datos:** MySQL 8  
- **Caché:** Redis 7  
- **Contenedores:** Docker Compose  
- **Middleware personalizado:** logging de peticiones  
- **Endpoints REST:** categorías, autores y publicaciones  
- **Healthcheck:** `/health/`  
- **Seed de datos iniciales:** comando `python manage.py seed`

---

## 🧩 Estructura del proyecto

```

blog-service/
│── blog_service/            ← configuración principal Django
│── core/                    ← middleware y comandos personalizados
│   └── management/commands/seed.py
│── authors/                 ← modelo Author
│── categories/              ← modelo Category
│── posts/                   ← modelo Post
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── manage.py
│── .env.example
│── README.md

````

---

## ⚙️ Variables de entorno (.env)

Ejemplo:

```bash
DB_HOST=mysql
DB_NAME=blogdb
DB_USER=devuser
DB_PASS=devpass
REDIS_HOST=redis
REDIS_PORT=6379
DEBUG=1
````

---

## 🐳 Cómo ejecutar el microservicio

1️⃣ **Construir y levantar contenedores**

```bash
docker compose up -d --build
```

2️⃣ **Aplicar migraciones**

```bash
docker compose exec blog python manage.py makemigrations
docker compose exec blog python manage.py migrate
```

3️⃣ **Cargar datos iniciales**

```bash
docker compose exec blog python manage.py seed
```

4️⃣ **Verificar contenedores**

```bash
docker ps
```

---

## 🔍 Endpoints principales

| Recurso     | Método                    | URL                | Descripción                           |
| ----------- | ------------------------- | ------------------ | ------------------------------------- |
| Healthcheck | GET                       | `/health/`         | Comprueba disponibilidad del servicio |
| Categorías  | GET / POST / PUT / DELETE | `/api/categories/` | CRUD de categorías                    |
| Autores     | GET / POST / PUT / DELETE | `/api/authors/`    | CRUD de autores                       |
| Posts       | GET / POST / PUT / DELETE | `/api/posts/`      | CRUD de publicaciones                 |

---

## 🧠 Middleware de logging

Archivo: `core/middleware.py`

```python
class RequestLogMiddleware:
    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        elapsed = time.time() - start
        logger.info(f"{request.method} {request.path} ({elapsed:.2f}s)")
        return response
```

Registra el tiempo de ejecución de cada petición en los logs del servidor.

---

## 🗄️ Seed de datos iniciales

Archivo: `core/management/commands/seed.py`

Crea registros de ejemplo para `Category`, `Author` y `Post`.

Ejecutar:

```bash
docker compose exec blog python manage.py seed
```

---

## 📦 Comandos útiles

```bash
# Detener todos los servicios
docker compose down

# Reiniciar solo el contenedor Django
docker compose restart blog

# Ver logs en vivo
docker compose logs -f blog
```

---

## 🧾 Versión del proyecto

**Día 3 — Backend Blog Service**
Microservicio funcional con Redis + MySQL + Docker.
Rama: `feature/blog-service`

---

## 👨‍💻 Autor

Desarrollado por **Matías Sicha & Edgar** — Proyecto de Microservicios
Período: *Día 3 – Backend (todas las salas excepto Sala 4)*

````

---

✅ Luego solo guarda el archivo y ejecuta:

```bash
git add README.md
git commit -m "Agregar README del Día 3"
git push
````