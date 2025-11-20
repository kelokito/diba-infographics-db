from src.models.users_model import UserRecord
import csv

def parse_csv_to_users(path):
    records = []
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(
                UserRecord(
                    id=int(row["id"]),
                    name=row["name"],
                    email=row["email"]
                )
            )
    return records
