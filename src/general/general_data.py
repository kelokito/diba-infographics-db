from src.models.general_model import GeneralRecord
import csv

def parse_csv_to_general(path):
    records = []
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(
                GeneralRecord(
                    id=int(row["id"]),
                    category=row["category"],
                    value=row["value"]
                )
            )
    return records
