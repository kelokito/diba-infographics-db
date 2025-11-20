select bib_id, library_id
from items
join bibliographics b
    on b.id = items.bib_id
