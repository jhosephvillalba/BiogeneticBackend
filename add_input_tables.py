import os
import pymysql
import logging
from dotenv import load_dotenv

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar variables de entorno
load_dotenv('db.env')

# Configuración de la base de datos
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'biogenetic'),
}

# SQL para crear tablas
create_inputs_table = """
CREATE TABLE IF NOT EXISTS inputs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    quantity_received FLOAT NOT NULL,
    escalarilla VARCHAR(100) NOT NULL,
    bull_id INT NOT NULL,
    status_id ENUM('pending', 'processing', 'completed', 'cancelled') DEFAULT 'pending' NOT NULL,
    lote VARCHAR(50) NOT NULL,
    fv DATETIME NOT NULL,
    quantity_taken FLOAT NOT NULL,
    total FLOAT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (bull_id) REFERENCES bulls(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX (id)
);
"""

create_outputs_table = """
CREATE TABLE IF NOT EXISTS outputs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    input_id INT NOT NULL,
    output_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    quantity_output FLOAT NOT NULL,
    remark TEXT,
    FOREIGN KEY (input_id) REFERENCES inputs(id) ON DELETE CASCADE,
    INDEX (id)
);
"""

def create_tables():
    """Crear las tablas en la base de datos"""
    conn = None
    try:
        conn = pymysql.connect(**db_config)
        
        with conn.cursor() as cursor:
            # Crear tabla de inputs
            logger.info("Creando tabla inputs...")
            cursor.execute(create_inputs_table)
            
            # Crear tabla de outputs
            logger.info("Creando tabla outputs...")
            cursor.execute(create_outputs_table)
            
        # Confirmar cambios
        conn.commit()
        logger.info("¡Tablas creadas con éxito!")
        
    except Exception as e:
        logger.error(f"Error al crear las tablas: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_tables() 