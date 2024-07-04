select state.id as id, state.Name as name, count(sighting.id) as sightings 
from state left join sighting
on state.id = sighting.state
and year(sighting.datetime) = 1931
group by state.id, state.Name