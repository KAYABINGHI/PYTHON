CREATE TABLE IF NOT EXISTS student(
    id SERIAL PRIMARY KEY,
    name VARCHAR (20) NOT NULL,
    email VARCHAR (100) NOT NULL UNIQUE,
    dob DATE,
    phone INTEGER NOT NULL UNIQUE,
    marks REAL CHECK (MARKS>-1 AND MARKS <101),
    is_married BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

INSERT INTO student (name,email,dob,phone,marks)
VALUES ('alice','alice@gmail.com','2002-3-23',0752369896,74.2);
