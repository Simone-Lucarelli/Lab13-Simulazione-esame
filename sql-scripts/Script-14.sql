select eo1.object_id as id_1, eo2.object_id as id_2,
	count(*) as exhibition_count
from exhibition_objects eo1, exhibition_objects eo2
where eo1.exhibition_id = eo2.exhibition_id 
	and eo1.object_id <> eo2.object_id
group by eo1.object_id, eo2.object_id