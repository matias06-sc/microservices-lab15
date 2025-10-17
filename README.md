## Laboratorio de Microservicios (Día 1: Fundamentos + Entorno Docker / Git)

[cite_start]Este documento resume las actividades y objetivos del **Día 1** del laboratorio práctico, enfocado en establecer la base teórica y el entorno de trabajo para una arquitectura de microservicios[cite: 7].

---

### 🎯 Objetivo General del Día 1

[cite_start]Comprender qué es una arquitectura de microservicios y preparar el entorno de trabajo para los siguientes días[cite: 9]. [cite_start]El grupo debe terminar el día con una base funcional en **Docker Compose**, donde cada servicio puede ser levantado de forma independiente[cite: 10].

### 🎬 Bloque de Video de Referencia

* [cite_start]**Video:** "Fundamentos + Docker + Git"[cite: 1].
* [cite_start]**Enlace:** `https://www.youtube.com/watch?v=wj766sxHZrM&t=20s`[cite: 2].
* [cite_start]**Duración a visualizar:** Desde el minuto **0:00** hasta el minuto **26:00**[cite: 4].
* **Temas obligatorios:**
    * [cite_start]Introducción, objetivos y qué son los microservicios (0:00 – 5:00)[cite: 6].
    * [cite_start]Principios: autonomía, acoplamiento, escalabilidad, observabilidad (5:00 – 10:00)[cite: 6].
    * [cite_start]Instalación y configuración de Docker Desktop y Docker Compose (WSL2) (10:00 – 20:00)[cite: 6].
    * [cite_start]Configuración de Git y GitHub (ramas `Main` / `Staging`) (20:00 – 24:00)[cite: 6].

### 🧩 Conceptos a Dominar (Día 1)

[cite_start]Al finalizar el día, se deben dominar los siguientes conceptos[cite: 11]:
* [cite_start]Diferencia entre monolito y microservicios[cite: 12].
* [cite_start]Principios básicos: autonomía, responsabilidad única, acoplamiento flexible, escalabilidad y observabilidad[cite: 13].
* [cite_start]Estructura de proyecto “multi-servicio”[cite: 14].
* [cite_start]Uso de **Docker** + **Docker Compose** para levantar contenedores[cite: 15].
* [cite_start]Control de versiones en **Git** (ramas `Main` y `Staging`)[cite: 16].

### 🛠️ Tareas Prácticas Paso a Paso

1.  [cite_start]**Crear la estructura base del proyecto**[cite: 18]:
    * [cite_start]Crear la carpeta principal: `mkdir microservices-lab`[cite: 19].
    * [cite_start]Crear las carpetas para los servicios: `mkdir auth-service blog-service email-service frontend reverse-proxy`[cite: 21].
    * [cite_start]Crear un `README.md` vacío dentro de cada carpeta[cite: 22].
2.  [cite_start]**Inicializar Git y GitHub**[cite: 23]:
    * [cite_start]Inicializar el repositorio local y el *commit* inicial[cite: 24, 25, 26, 27].
    * [cite_start]Vincular el repo remoto y hacer el *push* a la rama `main`[cite: 28, 29, 30].
3.  [cite_start]**Preparar el entorno Docker Compose**[cite: 31]:
    * [cite_start]Crear el archivo **`docker-compose.yml`** en la raíz[cite: 32].
    * [cite_start]Configurar los servicios **`postgres`** (puerto 5432) y **`redis`** (puerto 6379)[cite: 35, 47, 44, 51].
    * [cite_start]Ejecutar `docker compose up -d` y verificar con `docker ps`[cite: 55, 56, 57].
4.  [cite_start]**Crear archivos de entorno**[cite: 59]:
    * [cite_start]Crear el archivo **`.env.example`** con las variables de conexión a PostgreSQL y Redis[cite: 61, 62, 63, 64, 65, 66].
    * [cite_start]Cada equipo debe copiarlo a **`.env`** local[cite: 67].
5.  [cite_start]**Registrar en README el diseño inicial**[cite: 68]:
    * [cite_start]Documentar en el `README.md` de la raíz la **Arquitectura inicial** de los microservicios y los **Servicios base** (PostgreSQL y Redis)[cite: 69, 71, 72, 73, 74, 75, 76, 77, 78, 79].

### 📦 Entregables del Día 1

| Entregable | Descripción |
| :--- | :--- |
| **Repo Git** | [cite_start]Subido a GitHub con estructura base y `.env.example`[cite: 85]. |
| **Docker Compose funcional** | [cite_start]Levanta PostgreSQL y Redis sin errores[cite: 85]. |
| **README documentado** | [cite_start]Incluye arquitectura y checklist[cite: 85]. |
| **Captura o video corto** | [cite_start]Mostrando los contenedores en ejecución (`docker ps`)[cite: 85].