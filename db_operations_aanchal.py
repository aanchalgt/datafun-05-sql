"""
SQL Operations 

Implement SQL statements and queries to perform additional operations and 
use Python to execute your SQL statements. You might create an additional table,
nsert new records, and perform data querying (with filters, sorting, and joining tables),
data aggregation, and record update and deletion.
"""

# import dependencies
import pathlib
import sqlite3
import logging

import pandas as pd

# Define the database file path
db_file_path = pathlib.Path("project.db")

###############################
# Logging Configuration
###############################
logging.basicConfig(
    filename='log.txt', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a')  # 'a' for append, so logs are added to the file


def execute_sql_from_file(db_file_path, sql_file):
    """Execute SQL commands from a file and log the results."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL from {sql_file}")
            print(f"Executed SQL from {sql_file}")
    except (sqlite3.Error, FileNotFoundError) as e:
        error_message = f"Error executing SQL from {sql_file}: {e}"
        logging.error(error_message)
        print(error_message)

def main():
    # Define paths for the SQL files
    sql_files = [
        pathlib.Path("sql/insert_records.sql"),
        pathlib.Path("sql/update_records.sql"),
        pathlib.Path("sql/delete_records.sql"),
        pathlib.Path("sql/query_aggregation.sql"),
        pathlib.Path("sql/query_filter.sql"),
        pathlib.Path("sql/query_sorting.sql"),
        pathlib.Path("sql/query_group_by.sql"),
        pathlib.Path("sql/query_join.sql"),
    ]

    # Execute each SQL file
    for sql_file in sql_files:
        execute_sql_from_file(db_file_path, sql_file)

    logging.info("Program ended")

if __name__ == "__main__":
    main()