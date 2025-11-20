from src.models.bibliographics_model import BibliographicRecord
from src.db.db_connection import run_export_sql
import csv


def download_bibliographics_data():
    sql_file = "src/db/queries/bibliographics_queries.sql"
    run_export_sql(sql_file)


def parse_csv_to_bibliographics(path):
    records = []
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='|')
        for row in reader:
            records.append(
                BibliographicRecord(
                    id=int(row["id"]),
                    call=row["call"],
                    cdu=row["cdu"],
                    year_edition=int(row["year_edition"]),
                    mat_type=row["mat_type"],
                    lang=row["lang"]
                )
            )
    return records


def update_bibliographics_data(path):
    # 1. Export SQL -> CSV file
    download_bibliographics_data()

    # 2. Parse CSV
    bibliographics = parse_csv_to_bibliographics(path)

    # 3. Generate analytics or dashboard profile
    generate_bibliographics_infographics(bibliographics)
