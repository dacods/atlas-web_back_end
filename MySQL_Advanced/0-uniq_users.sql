-- Script that creates a table
CREATE TABLE users IF NOT EXISTS(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE, 
    email VARCHAR(255)
    ); 