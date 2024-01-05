from cs50 import SQL

def updateElo(winnerID, loserID, db):
    # Retrieve database and score values
    SCORE = {"win": 1, "lose": 0}
    
    db.execute("BEGIN TRANSACTION")

    winner = db.execute("SELECT id, elo FROM girls WHERE id = ?", int(winnerID))[0]
    loser = db.execute("SELECT id, elo FROM girls WHERE id = ?", int(loserID))[0]

    # Calculate new ELOS
    newWinnerELO = winner["elo"] + 100 * (SCORE["win"] - expectedScore(winner["elo"], loser["elo"]))
    newLoserELO = loser["elo"] + 100 * (SCORE["lose"] - expectedScore(loser["elo"], winner["elo"]))

    # Input elos into database
    db.execute("UPDATE girls SET elo = ? WHERE id = ?", round(newWinnerELO), winnerID)
    db.execute("UPDATE girls SET elo = ? WHERE id = ?", round(newLoserELO), loserID)

    db.execute("COMMIT")

def expectedScore(ratingA, ratingB):
    return 1/(1 + 10**((ratingB - ratingA)/400))