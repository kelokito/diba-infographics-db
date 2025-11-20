from src.db.db_connection import get_connection

class BibliographicsRepository:

    @staticmethod
    def insert_records(records):
        conn = get_connection()
        cur = conn.cursor()

        sql = """
            INSERT INTO bibliographics (
                id, call, cdu, year_edition, mat_type, lang
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """

        for r in records:
            cur.execute(sql, (r.id, r.call, r.cdu, r.year_edition, r.mat_type, r.lang))

        conn.commit()
        conn.close()
