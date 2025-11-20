import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def run_export_sql(sql_file: str):
    """Loads SQL, replaces {DATA_PATH}, executes COPY export."""
    data_path = os.getenv("DATA_PATH")
    if not data_path:
        raise ValueError("DATA_PATH not found in .env")

    with open(sql_file, "r", encoding="utf8") as f:
        sql = f.read().replace("{DATA_PATH}", data_path)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

    print(f"✔ Export completed using {sql_file}")
