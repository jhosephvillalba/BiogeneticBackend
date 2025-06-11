import pymysql
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv("db.env")

# Configuración de la base de datos
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Conexión a la base de datos
conn_str = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(conn_str)

def update_bull_register_nullable():
    """Hace que el campo register en la tabla bulls sea opcional (nullable)"""
    with engine.begin() as connection:
        sql = text("ALTER TABLE bulls MODIFY COLUMN register VARCHAR(50) NULL;")
        connection.execute(sql)
        print("¡Campo register de la tabla bulls modificado correctamente a nullable!")

if __name__ == "__main__":
    update_bull_register_nullable() 