import sqlite3


class DBUtils:
    def __init__(self, db_file_path):
        self._db_file_path = db_file_path

    def _les_sqlite_db(self):
        with sqlite3.connect(self._db_file_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cur.fetchall()
            db_contents = {}
            for table_name in tables:
                cur.execute(f"SELECT * FROM {table_name[0]}")
                table_data = cur.fetchall()
                column_names = [description[0]
                                for description in cur.description]
                db_contents[table_name[0]] = {
                    "columns": column_names, "rows": table_data}
        return db_contents

    def les_db(self, *tabeller):
        """
        Test metode brukt til å lese databasen
        """
        db_contents = self._les_sqlite_db()

        for table, data in db_contents.items():
            if table not in tabeller and tabeller:
                continue
            print(f"Table: {table}")
            print("Columns:", data["columns"])
            for row in data["rows"]:
                print(row)
            print("\n")

    def load_intial_data(self):
        with sqlite3.connect(self._db_file_path) as con:
            cursor = con.cursor()
            intial_data_sql_path = "prosjekt_del_2/insert-db.sql"
            with open(intial_data_sql_path, 'r') as sql_file:
                sql_script = sql_file.read()
                cursor.executescript(sql_script)
            con.commit()
