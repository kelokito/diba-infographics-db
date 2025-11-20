from src.models.bibliographics_model import BibliographicRecord

def parse_csv_to_bibliographics(path):
    import csv
    records = []
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(
                BibliographicRecord(
                    id=int(row["id"]),
                    title=row["title"],
                    author=row["author"],
                    year=int(row["year"])
                )
            )
    return records
