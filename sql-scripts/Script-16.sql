SELECT eo1.object_id as main_object,
       GROUP_CONCAT(eo2.object_id ORDER BY eo2.object_id) as connected_objects
FROM exhibition_objects eo1
JOIN exhibition_objects eo2 ON eo1.exhibition_id = eo2.exhibition_id 
                             AND eo1.object_id <> eo2.object_id
GROUP BY eo1.object_id;