#q1
SELECT name FROM world
  WHERE name LIKE 'Y%'

#q2
SELECT name FROM world
  WHERE name LIKE '%y'

#q3
SELECT name FROM world
  WHERE name LIKE '%x%'

#q4
SELECT name FROM world
  WHERE name LIKE '%land'

#q5
SELECT name FROM world
  WHERE name LIKE 'C%' AND name LIKE '%ia'

#q6
SELECT name FROM world
  WHERE name LIKE '%oo%'

#q7
SELECT name FROM world
  WHERE name LIKE '%a%a%a%'

#q8
SELECT name FROM world
 WHERE name LIKE '_t%'
ORDER BY name

#q9
SELECT name FROM world
 WHERE name LIKE '%o__o%'

#q10
SELECT name FROM world
 WHERE LENGTH(name) = 4

#q11
SELECT name
  FROM world
 WHERE name = capital

#q12
SELECT name
FROM world
WHERE CONCAT(name,' ','City') = capital

#q13
SELECT capital,name
FROM world
WHERE capital LIKE CONCAT('%',name,'%')

#q14
SELECT capital,name
FROM world
WHERE capital LIKE CONCAT(name,'%') AND name != capital