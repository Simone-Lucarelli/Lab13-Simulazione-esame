select year(datetime) as year, count(*) as sightings
from sighting s
group by year(datetime)
