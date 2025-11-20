select id, call, cdu, year_edition, b.mat_type , lang
from bibliographics
join bib_materials bm
	on bm.id = b.mat_type
