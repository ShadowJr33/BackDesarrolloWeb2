import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DATABASE = os.getenv("DATABASE", "backDesarrolloWeb")
USERNAME = "root"
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", 3306)
print(f"Conectando a la base de datos {DATABASE} en {HOST}:{PORT} como {USERNAME}")

# SQLAlchemy necesita esta URL en formato especial
DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# Crear el engine con manejo automático de pool
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Creador de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para todos los modelos ORM
Base = declarative_base()

if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("✅ Conexión exitosa a la base de datos.")
    except Exception as e:
        print(f"❌ Error al conectar: {e.with_traceback}")

