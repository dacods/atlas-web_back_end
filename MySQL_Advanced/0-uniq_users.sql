-- Script that creates a table
CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE, 
    email VARCHAR(255)
    ); 