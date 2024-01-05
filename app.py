from cs50 import SQL
from flask import Flask, render_template, request, redirect
from helpers import updateElo

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")

# CONSTANTS
MAX_ID = db.execute("SELECT COUNT(id) as counter FROM girls")[0]["counter"]

# On load redirect to battle
@app.route("/", methods=["GET", "POST"])
def battle():

    girls = db.execute("SELECT id, elo FROM girls ORDER BY elo DESC")

    # Generate IDS
    if request.method == "GET":
        girl1 = {"id": 0, "name": "John Doe", "elo": None}
        girl2 = {"id": 0, "name": "John", "elo": None}
        return render_template("battle.html", MAX_ID=MAX_ID, girl1=girl1, girl2=girl2, girls=girls)

    else:
        # If ID generation request
        if request.form.get("id1") != None and request.form.get("id2") != None:

            # Get IDs
            id1 = request.form.get("id1")
            id2 = request.form.get("id2")

            #Validate IDS
            if not id1 in [str(x) for x in range(1, MAX_ID + 1)] or not id2 in [str(x) for x in range(1, MAX_ID + 1)] or id1 == id2:
                return redirect("/")       

            #Query database for girls
            girl1 = db.execute("SELECT id, elo FROM girls WHERE id = ?", int(id1))[0]
            girl2 = db.execute("SELECT id, elo FROM girls WHERE id = ?", int(id2))[0]     

            # Render battle
            return render_template("battle.html", MAX_ID=MAX_ID, girl1=girl1, girl2=girl2, girls=girls)        

        # If ELO change request    
        elif request.form.get("winner") != None and request.form.get("loser") != None:

            # Get IDS
            winnerID = request.form.get("winner")
            loserID = request.form.get("loser")

            # Validate IDS
            if not winnerID in [str(x) for x in range(1, MAX_ID + 1)] or not loserID in [str(x) for x in range(1, MAX_ID + 1)] or winnerID == loserID:
                return redirect("/")          

            # Update elo
            updateElo(winnerID, loserID, db)

            # Generate new IDs
            return redirect("/")

        else:
            # Generate new IDS
            return redirect("/")    

if __name__ == "__main__":
    app.run(debug=True)
