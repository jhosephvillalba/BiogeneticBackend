import os
from decouple import config, Csv
from dotenv import load_dotenv

# Cargar variables de entorno
try:
    load_dotenv(".env")  # Intentar primero con .env
except:
    pass

try:
    load_dotenv("db.env")  # Luego intentar con db.env
except:
    pass

class Settings:
    """Configuración de la aplicación"""
    APP_NAME: str = "BioGenetic API"
    DEBUG: bool = config('DEBUG', default=True, cast=bool)
    API_HOST: str = config('API_HOST', default='0.0.0.0')
    API_PORT: int = config('API_PORT', default=8000, cast=int)
    SECRET_KEY: str = config('SECRET_KEY', default='b9ee2529f3e77b0e32c24b8774f15e8fa7c1058e1f2427f4d0b0063ed23abf2f')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config('ACCESS_TOKEN_EXPIRE_MINUTES', default=30, cast=int)
    
    # Configuración de la base de datos MySQL
    DB_HOST: str = config('DB_HOST', default='localhost')
    DB_PORT: int = config('DB_PORT', default=3306, cast=int)
    DB_USER: str = config('DB_USER', default='root')
    DB_PASSWORD: str = config('DB_PASSWORD', default='')
    DB_NAME: str = config('DB_NAME', default='biogenetic')

settings = Settings() 