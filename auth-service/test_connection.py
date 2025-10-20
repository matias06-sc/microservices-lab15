import os
import psycopg2
import redis

# -------------------------------
# Variables de entorno
# -------------------------------
POSTGRES_USER = os.getenv("POSTGRES_USER", "devuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "main_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db_postgres")  # contenedor
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

REDIS_HOST = os.getenv("REDIS_HOST", "cache_redis")  # contenedor
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# -------------------------------
# Prueba de conexión a PostgreSQL
# -------------------------------
print("🔍 Probando conexión con PostgreSQL...")
try:
    conn = psycopg2.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DB,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        options='-c client_encoding=UTF8'
    )
    print("✅ Conectado correctamente a PostgreSQL")
    conn.close()
except Exception as e:
    print("❌ Error conectando a PostgreSQL:", e)

# -------------------------------
# Prueba de conexión a Redis
# -------------------------------
print("\n🔍 Probando conexión con Redis...")
try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    r.set("test", "ok")
    value = r.get("test")
    print(f"✅ Conectado a Redis, valor guardado: {value}")
except Exception as e:
    print("❌ Error conectando a Redis:", e)
