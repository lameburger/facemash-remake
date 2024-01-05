import sqlite3
import os
from cs50 import SQL

# Specify the path to your SQLite database file
db = SQL("sqlite:///database.db")

# Close any existing connections to the database
conn = sqlite3.connect(db)
conn.close()

# Delete the existing database file
if os.path.exists(db):
    os.remove(db)
    print(f"The database at {db} has been deleted.")