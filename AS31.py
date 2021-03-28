#t1
SELECT matchid,player
FROM goal
WHERE teamid LIKE 'GER'

#t2
SELECT id,stadium,team1,team2
  FROM game
WHERE ID LIKE '1012'

#t3
SELECT player,teamid,stadium,mdate
  FROM game JOIN goal ON (id=matchid)
WHERE teamid LIKE 'GER'

#t4
SELECT team1, team2, player
FROM game JOIN goal ON (id=matchid)
WHERE player LIKE 'Mario%'

#t5
SELECT player, teamid, coach,gtime
  FROM goal JOIN eteam ON (teamid=id)
 WHERE gtime<=10

#t6
SELECT mdate,teamname
FROM game JOIN eteam ON (team1=eteam.id)
WHERE coach LIKE 'Fernando Santos'

#t7
SELECT player
FROM game JOIN goal ON (id=matchid)
WHERE stadium LIKE 'National Stadium, Warsaw'

#t8
SELECT DISTINCT(player)
  FROM game JOIN goal ON matchid = id
    WHERE ((team1='GER' AND team2 LIKE'%') OR (team1 LIKE '%' AND team2 = 'GER')) AND teamid != 'GER'

#t9
SELECT teamname, COUNT(teamid)
  FROM eteam JOIN goal ON id=teamid
 GROUP BY teamname

#t10
SELECT stadium, COUNT(teamid)
FROM game JOIN goal ON id=matchid
GROUP BY stadium

#t11
SELECT matchid,mdate, COUNT(teamid)
  FROM game JOIN goal ON id=matchid
 WHERE (team1 = 'POL' OR team2 = 'POL')
GROUP BY matchid,mdate

#t12
SELECT matchid,mdate, COUNT(teamid)
  FROM game JOIN goal ON id=matchid
 WHERE teamid = 'GER'
GROUP BY matchid,mdate