from src.db.db_connection import get_connection

class BibliographicsRepository:

    @staticmethod
    def insert_records(records):
        conn = get_connection()
        cur = conn.cursor()
        sql = """INSERT INTO bibliographics_info (id, title, author, year)
                 VALUES (%s, %s, %s, %s)
                 ON CONFLICT (id) DO NOTHING;"""
        for r in records:
            cur.execute(sql, (r.id, r.title, r.author, r.year))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM bibliographics_info")
        data = cur.fetchall()
        conn.close()
        return data
