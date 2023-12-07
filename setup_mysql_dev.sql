-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS recipes_dev_db;
CREATE USER IF NOT EXISTS 'recipes_dev'@'localhost' IDENTIFIED BY 'recipes_dev_pwd';
GRANT ALL PRIVILEGES ON `recipes_dev_db`.* TO 'recipes_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'recipes_dev'@'localhost';
FLUSH PRIVILEGES;
