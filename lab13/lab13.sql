.read data.sql

CREATE TABLE bluedog AS
  SELECT stu.color AS color, stu.pet AS pet
  FROM students AS stu
  WHERE stu.pet = "dog" AND stu.color = "blue";


CREATE TABLE bluedog_songs AS
  SELECT stu.color AS color, stu.pet AS pet, stu.song AS song
  FROM students AS stu
  WHERE stu.pet = "dog" AND stu.color = "blue";


CREATE TABLE smallest_int_having AS
  SELECT time AS time, smallest AS minimum
  FROM students GROUP BY smallest HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT stu1.pet AS pet, stu2.song AS song, stu1.color AS color1, stu2.color AS color2
  FROM students AS stu1, students AS stu2
  WHERE stu1.pet = stu2.pet AND stu1.song = stu2.song AND stu1.time < stu2.time;


CREATE TABLE sevens AS
  SELECT stu.seven AS seven
  FROM students AS stu, numbers AS num
  WHERE stu.time = num.time AND stu.number = 7 AND num.'7' = "True";


CREATE TABLE avg_difference AS
  SELECT ROUND(AVG(ABS(number - smallest))) AS avgdiff
  FROM students;




