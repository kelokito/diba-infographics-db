-- bibliographics export
-- {DATA_PATH} will be replaced by run_export_sql()

COPY (
    SELECT 
        b.id,
        b.call,
        b.cdu,
        b.year_edition,
        b.mat_type,
        b.lang
    FROM bibliographics b
    JOIN bib_materials bm
        ON bm.id = b.mat_type
)
TO '{DATA_PATH}/bibliographics.csv'
WITH CSV HEADER DELIMITER '|' ENCODING 'UTF8';
