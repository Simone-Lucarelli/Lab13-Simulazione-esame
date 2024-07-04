select n.state1, n.state2, count(*) as peso 
from neighbor n left join sighting s1 
on  year(s1.datetime) = 2010 and s1.state = n.state1
left join sighting s2 
on year(s2.datetime) = 2010 and s2.state = n.state2
and ABS(datediff(s1.datetime, s2.datetime)) <= 1 
where n.state1 < n.state2 
group by n.state1, n.state2