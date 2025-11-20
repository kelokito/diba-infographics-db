import os
from dotenv import load_dotenv

from bibliographics.bibliographics_data import parse_csv_to_bibliographics
from bibliographics.bibliographics_repository import BibliographicsRepository

from users.users_data import parse_csv_to_users
from users.users_repository import UsersRepository

from general.general_data import parse_csv_to_general
from general.general_repository import GeneralRepository


def ingest_bibliographics(path):
    print(f"📘 Ingesting bibliographics from {path}...")
    records = parse_csv_to_bibliographics(path)
    BibliographicsRepository.insert_records(records)
    print(f"✔ Bibliographics ingestion completed ({len(records)} rows).")


def ingest_users(path):
    print(f"👥 Ingesting users from {path}...")
    records = parse_csv_to_users(path)
    UsersRepository.insert_records(records)
    print(f"✔ Users ingestion completed ({len(records)} rows).")


def ingest_general(path):
    print(f"📊 Ingesting general data from {path}...")
    records = parse_csv_to_general(path)
    GeneralRepository.insert_records(records)
    print(f"✔ General ingestion completed ({len(records)} rows).")


def main():
    load_dotenv()

    # ------------ CHANGE THESE PATHS AS NEEDED ------------
    bibliographics_path = "data/bibliographics.csv"
    users_path = "data/users.csv"
    general_path = "data/general.csv"
    # ------------------------------------------------------

    print("\n🚀 Starting full ingestion...\n")

    ingest_bibliographics(bibliographics_path)
    ingest_users(users_path)
    ingest_general(general_path)

    print("\n🎉 All data ingestion completed successfully!\n")


if __name__ == "__main__":
    main()
