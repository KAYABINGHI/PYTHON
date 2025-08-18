-- read all columns 
-- SELECT * FROM student;

-- read only name and email
-- SELECT name, email, from student;

-- SELECT * from student
-- WHERE email='alice@gmail.com'
-- OR
-- -- email = 'john@gmail.com'

-- SELECT * from student
-- WHERE pocket_money > 10
-- AND pocket_money < 100

SELECT *from student 
ORDER BY name ASC
LIMIT 2
