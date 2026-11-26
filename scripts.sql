-- Creacion de base de datos
CREATE DATABASE IF NOT EXISTS centro_medico
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Creacion de usuario y asignacion de permisos
CREATE USER IF NOT EXISTS 'admin_vida'@'localhost' IDENTIFIED BY 'Vida2026*';
GRANT ALL PRIVILEGES ON centro_medico.* TO 'admin_vida'@'localhost';
FLUSH PRIVILEGES;
