CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone INTEGER,
    marks REAL
);

INSERT INTO student (name,email,dob,phone,marks)
VALUES ('mwenda','moen@gmail.com','2002-05-13',254113963,88.2);

SELECT * FROM student

