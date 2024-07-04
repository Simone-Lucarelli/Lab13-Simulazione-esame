select
	tab1.loc1, tab1.loc2, count(distinct tab1.type)
from	
	(select
		c1.Localization as loc1, c2.Localization as loc2,
		c1.GeneID as id1, c2.GeneID as id2, i.type as type
	from
		interactions i, classification c1, classification c2
	where
		i.GeneID1 = c1.GeneID and i.GeneID2 = c2.GeneID
		and c1.Localization <> c2.Localization) as tab1
group by
	tab1.loc1, tab1.loc2