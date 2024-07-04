select distinct c_1, c_2, sum(expr)
from (
select distinct g1.Chromosome as c_1, g2.Chromosome as c_2, 
g1.GeneID as g_id1, g2.GeneID as g_id2, i.Expression_Corr as expr
from interactions i, genes g1, genes g2
where g1.GeneID = i.GeneID1 and g2.GeneID  = i.GeneID2
	and g1.Chromosome <> g2.Chromosome
	and g1.Chromosome = 5
	and g2.Chromosome = 11 
order by g1.Chromosome ) as t
group by c_1, c_2