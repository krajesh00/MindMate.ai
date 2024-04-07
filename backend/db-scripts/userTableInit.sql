CREATE TABLE users (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    passphrase VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    age INT NOT NULL,
    username VARCHAR(50) NOT NULL
);

INSERT INTO users (firstname, lastname, passphrase, email, age, username) VALUES ('John', 'Doe', 'password', 'email @gmail.com', 25, 'johndoe');