-- Tabla de inputs
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
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Tabla de outputs
CREATE TABLE IF NOT EXISTS outputs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    input_id INT NOT NULL,
    output_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    quantity_output FLOAT NOT NULL,
    remark TEXT,
    FOREIGN KEY (input_id) REFERENCES inputs(id) ON DELETE CASCADE
); 