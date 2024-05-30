-- Active: 1715043174887@@127.0.0.1@3306@
DROP DATABASE IF EXISTS shark_db;

CREATE DATABASE shark_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE shark_db;

CREATE TABLE permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    UNIQUE KEY (name)
);

INSERT INTO permissions (name)
 VALUES 
 ('barber'),
  ('cliente')

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(255),
    last_name VARCHAR(255),
    phone VARCHAR(255),
    password VARCHAR(255),
    email VARCHAR(255),
    permissions_id INT NOT NULL DEFAULT 1,
    UNIQUE KEY (email),
    FOREIGN KEY (permissions_id) REFERENCES permissions (id)
);
DROP TABLE IF EXISTS citas;
CREATE TABLE citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dia DATE NOT NULL,
    hora TIME NOT NULL,
    barber_id INT NOT NULL,
    cliente_id INT NOT NULL,
    status ENUM('pending', 'done', 'canceled') NOT NULL DEFAULT 'pending',
    FOREIGN KEY (barber_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (cliente_id) REFERENCES users (id) ON DELETE CASCADE
);

INSERT INTO users (name, last_name, password, email, permissions_id)
 VALUES 
 ('John', 'Doe', '123456', 'john@doe.com', 1),
 ('Jane', 'Doe', '123456', 'jane@doe.com', 2)

INSERT INTO citas (dia, hora, barber_id, cliente_id)
 VALUES 
 ('2022-01-01', '10:00:00', 1, 1)