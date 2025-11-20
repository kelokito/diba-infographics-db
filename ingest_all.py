import os
from dotenv import load_dotenv

from bibliographics.bibliographics_data import update_bibliographics_data

from users.users_data import parse_csv_to_users
from users.users_repository import UsersRepository

from general.general_data import parse_csv_to_general
from general.general_repository import GeneralRepository


def get_path(filename: str) -> str:
    """Return full path from DATA_PATH env variable."""
    data_path = os.getenv("DATA_PATH")
    if not data_path:
        raise ValueError("DATA_PATH is not defined in .env file")
    return os.path.join(data_path, filename)


def ingest_bibliographics():
    path = get_path("bibliographics.csv")
    print(f"📘 Ingesting bibliographics from {path}...")

    update_bibliographics_data(path)

    print(f"✔ Bibliographics ingestion completed.")


def ingest_users():
    path = get_path("users.csv")
    print(f"👥 Ingesting users from {path}...")

    records = parse_csv_to_users(path)
    UsersRepository.insert_records(records)

    print(f"✔ Users ingestion completed ({len(records)} rows).")


def ingest_general():
    path = get_path("general.csv")
    print(f"📊 Ingesting general data from {path}...")

    records = parse_csv_to_general(path)
    GeneralRepository.insert_records(records)

    print(f"✔ General ingestion completed ({len(records)} rows).")


def main():
    load_dotenv()

    print("\n🚀 Starting full ingestion...\n")

    ingest_bibliographics()
    ingest_users()
    ingest_general()

    print("\n🎉 All data ingestion completed successfully!\n")


if __name__ == "__main__":
    main()
