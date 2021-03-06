.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number 
  FROM students AS a, fa17students AS b
  WHERE a.date = b.date AND a.color = b.color AND a.pet = b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT a.seven 
  FROM students as a, checkboxes as b
  WHERE a.number = 7 AND b.'7' = 'True' AND a.time = b.time;


-- Q7
CREATE TABLE fa17favnum AS
  SELECT a.number, COUNT(*) AS count
  FROM fa17students as a
  GROUP BY a.number 
  ORDER BY count DESC
  LIMIT 1
  ;


CREATE TABLE fa17favpets AS
  SELECT pet, COUNT(*)
  FROM fa17students
  GROUP BY pet
  ORDER BY -COUNT(*)
  LIMIT 10;


CREATE TABLE sp18favpets AS
  SELECT pet, COUNT(*)
  FROM students
  GROUP BY pet
  ORDER BY -COUNT(*)
  LIMIT 10;


CREATE TABLE sp18dog AS
  SELECT pet, COUNT(*)
  FROM students
  WHERE pet = 'dog'
  GROUP BY pet;

-- no group by here, other wise, the pet column would be the result after groupby, like a dog 11, dog 10
CREATE TABLE sp18alldogs AS
  SELECT pet, COUNT(*)
  FROM students
  WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*)
  FROM obedience 
  WHERE seven = '7'
  GROUP BY denero
  ORDER BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*)
  FROM students
  GROUP BY smallest
  ORDER BY smallest;
