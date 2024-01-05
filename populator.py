from cs50 import SQL
import os

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")

for count in range(1, len(os.listdir("static/images")) + 1):
    db.execute("INSERT INTO girls (elo) VALUES (1400)")