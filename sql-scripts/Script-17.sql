select n1.state1, n1.state2, count(*) as sightings
from(select state, count(*) as sightings
		from sighting where year(datetime) = %s and shape = %s
		group by state) as s1,
		(select state, count(*) as sightings
		from sighting where year(datetime) = %s and shape = %s
		group by state) as s2,
		neighbor n1
where s1.state = n1.state1 and s2.state = n1.state2
