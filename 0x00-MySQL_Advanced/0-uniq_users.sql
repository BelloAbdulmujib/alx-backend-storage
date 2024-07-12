'''Creates a table users with some requirements.
'''

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULLAUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
