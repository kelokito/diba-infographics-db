select id, sex as genre, birth_date
from users
    where ptype IN (10, 11, 12, 21, 22, 23, 31)