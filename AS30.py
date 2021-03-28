#t1
SELECT name, continent, population FROM world

#t2
SELECT name FROM world
WHERE population = 200000000

#t3
SELECT name, gdp/population
FROM world
WHERE population >= 200000000

#t4
SELECT name, population/1000000
FROM world
WHERE continent = 'South America'

#t5
SELECT name, population
FROM world
WHERE name IN ('France', 'Germany', 'Italy')

#t6
SELECT name
FROM world
WHERE ('United') IN name

#t7
SELECT name, population, area
FROM world
WHERE area > 3000000 or population > 250000000

#t8
SELECT name, population, area
FROM world
WHERE area > 3000000 xor population >250000000

#t9
SELECT name, ROUND(population/1000000,2), ROUND(gdp/1000000000,2)
FROM world
WHERE continent = 'South America'

#t10
SELECT name, ROUND(gdp/population,-3)
FROM world
WHERE gdp>=1000000000000

#t11
SELECT name, capital
FROM world
WHERE LENGTH(name) = LENGTH(capital);

#t12
SELECT name, capital
FROM world
WHERE LEFT(name,1) = LEFT(capital, 1) AND name != capital