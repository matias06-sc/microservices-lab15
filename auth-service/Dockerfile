# Imagen base de Python
FROM python:3.11-slim

# Evitar creación de archivos .pyc y salida buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Copiar requirements y luego instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del proyecto
COPY . .

# Exponer puerto de Django
EXPOSE 8000

# Comando para desarrollo: runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
