import sqlite3

def read_sqlite_db(db_path):
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Fetch all table names
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    # Dictionary to hold table data
    db_contents = {}

    # Iterate over each table and fetch its contents
    for table_name in tables:
        cur.execute(f"SELECT * FROM {table_name[0]}")
        # Fetch all rows from table
        table_data = cur.fetchall()
        # Fetch column names
        column_names = [description[0] for description in cur.description]
        # Store table data using column names as keys
        db_contents[table_name[0]] = {"columns": column_names, "rows": table_data}

    # Close connection
    conn.close()
    return db_contents

# Replace 'your_database_file.db' with the path to your SQLite database file
db_path = 'Theatre.db'
db_contents = read_sqlite_db(db_path)

# You can now work with `db_contents` dictionary to access your data
# For example, to print all table names and their contents:
for table, data in db_contents.items():
    print(f"Table: {table}")
    print("Columns:", data["columns"])
    for row in data["rows"]:
        print(row)
    print("\n")  # Add an empty line for better readability between tables
