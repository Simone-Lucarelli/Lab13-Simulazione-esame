select s.state as state1, s2.state as state2, count(*) as sightings
from sighting s, sighting s2, neighbor n 
where YEAR(s.datetime) = YEAR(s2.datetime)
	and year(s2.datetime) = 1990
	and s.state <> s2.state
	and s.state = n.state1 
	and s2.state = n.state2
	and DATEDIFF(s.datetime, s2.datetime) < 10
group by s.state, s2.state