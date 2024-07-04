select distinct ID, name, sum(salary)
from teams t, salaries s 
where year = 1980 and s.teamID = t.ID 
group by id, name