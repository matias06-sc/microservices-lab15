## Laboratorio de Microservicios (Día 1: Fundamentos + Entorno Docker / Git)

Este documento resume las actividades y objetivos del **Día 1** del laboratorio práctico, enfocado en establecer la base teórica y el entorno de trabajo para una arquitectura de microservicios.

---

### 🎯 Objetivo General del Día 1

Comprender qué es una arquitectura de microservicios y preparar el entorno de trabajo para los siguientes días. El grupo debe terminar el día con una base funcional en **Docker Compose**, donde cada servicio puede ser levantado de forma independiente.

### 🎬 Bloque de Video de Referencia

* **Video:** "Fundamentos + Docker + Git"[cite: 1].
* **Enlace:** `https://www.youtube.com/watch?v=wj766sxHZrM&t=20s`.
* **Duración a visualizar:** Desde el minuto **0:00** hasta el minuto **26:00**.
* **Temas obligatorios:**
    * Introducción, objetivos y qué son los microservicios (0:00 – 5:00).
    * Principios: autonomía, acoplamiento, escalabilidad, observabilidad (5:00 – 10:00).
    * Instalación y configuración de Docker Desktop y Docker Compose (WSL2) (10:00 – 20:00).
    * Configuración de Git y GitHub (ramas `Main` / `Staging`) (20:00 – 24:00).

### 🧩 Conceptos a Dominar (Día 1)

Al finalizar el día, se deben dominar los siguientes conceptos[cite: 11]:
* Diferencia entre monolito y microservicios.
* Principios básicos: autonomía, responsabilidad única, acoplamiento flexible, escalabilidad y observabilidad.
* Estructura de proyecto “multi-servicio”.
* Uso de **Docker** + **Docker Compose** para levantar contenedores.
* Control de versiones en **Git** (ramas `Main` y `Staging`).

### 🛠️ Tareas Prácticas Paso a Paso

1.  **Crear la estructura base del proyecto**:
    * Crear la carpeta principal: `mkdir microservices-lab`.
    * Crear las carpetas para los servicios: `mkdir auth-service blog-service email-service frontend reverse-proxy`.
    * Crear un `README.md` vacío dentro de cada carpeta.
2.  **Inicializar Git y GitHub**:
    * Inicializar el repositorio local y el *commit* inicial.
    * Vincular el repo remoto y hacer el *push* a la rama `main`.
3.  **Preparar el entorno Docker Compose**:
    * Crear el archivo **`docker-compose.yml`** en la raíz.
    * Configurar los servicios **`postgres`** (puerto 5432) y **`redis`** (puerto 6379).
    * Ejecutar `docker compose up -d` y verificar con `docker ps`.
4.  **Crear archivos de entorno**:
    * Crear el archivo **`.env.example`** con las variables de conexión a PostgreSQL y Redis.
    * Cada equipo debe copiarlo a **`.env`** local.
5.  **Registrar en README el diseño inicial**:
    * Documentar en el `README.md` de la raíz la **Arquitectura inicial** de los microservicios y los **Servicios base** (PostgreSQL y Redis).

### 📦 Entregables del Día 1

| Entregable | Descripción |
| :--- | :--- |
| **Repo Git** | Subido a GitHub con estructura base y `.env.example`. |
| **Docker Compose funcional** | Levanta PostgreSQL y Redis sin errores. |
| **README documentado** | Incluye arquitectura y checklist. |
| **Captura o video corto** | Mostrando los contenedores en ejecución (`docker ps`).
