-- Modificar la columna register en la tabla bulls para que sea opcional (nullable)
ALTER TABLE bulls MODIFY COLUMN register VARCHAR(50) NULL; 