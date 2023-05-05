import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

date = date.today()

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    users = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    portfolio = db.execute("SELECT * FROM portfolio WHERE user_id = ?", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    grandTotal = db.execute("SELECT total FROM grandtotal WHERE user_id = ?", session["user_id"])
    # update total value of each stock
    for data in portfolio:
        data["total"] = data["price"] * data["shares"]
    # grand total stocks’ value
    if not grandTotal:
        return render_template("index.html", users=users, portfolio=portfolio, grandTotal=0)
    if not portfolio:
        print(grandTotal)
        return render_template("index.html", users=users, portfolio=portfolio, grandTotal=grandTotal[0]["total"])
    else:
        sum = db.execute("SELECT SUM(total) FROM portfolio WHERE user_id = ?", session["user_id"])
        grandTotal = sum[0]["SUM(total)"] + cash[0]["cash"]
        db.execute("UPDATE grandtotal SET total = ? WHERE user_id = ?", grandTotal, session["user_id"])
        return render_template("index.html", users=users, portfolio=portfolio, grandTotal=grandTotal)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # get data
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        response = lookup(symbol)

        # check for correct user input or if the user is out of money
        if not symbol:
            return apology("must provide symbol", 400)
        if not shares:
            return apology("must provide shares", 400)
        if not shares.isdigit():
            return apology("must provide whole number", 400)
        if not response:
            return apology("must provide valid symbol", 400)
        if len(symbol) > 5:
            return apology("must provide valid symbol", 400)

        # get data from db
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        print(cash)
        portfolio = db.execute("SELECT symbol FROM portfolio WHERE user_id = ?", session["user_id"])
        # get data from json
        name = response["name"]
        price = int(response["price"])
        # caclulate total price of shares
        total = price * int(shares)
        if total > cash[0]["cash"]:
            return apology("can't afford", 400)
        # calculate remaining cash
        remainingCash = cash[0]["cash"] - total

        # count matching stocks
        count = 0
        # check if portfolio is empty, if it is add the first stock
        if portfolio == []:
            db.execute("INSERT INTO portfolio (user_id, symbol, name, shares, price, total) VALUES (?, ?, ?, ?, ?, ?)",
                       session["user_id"], symbol, name, shares, price, total)
        else:
            # loop through stocks and increment if the new stock is in the portofolio, update counter if it is, and add the transaction to history
            for i in range(len(portfolio)):
                if symbol == portfolio[i]["symbol"]:
                    db.execute("UPDATE portfolio SET shares = shares + ? WHERE user_id = ? AND symbol = ?",
                               shares, session["user_id"], symbol)
                    db.execute("INSERT INTO history (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
                               session["user_id"], symbol, shares, price, date)
                    count += 1
                    break
            # if counter is 0 there are no matching stocks so add a new stock and add the transaction to history
            if count == 0:
                db.execute("INSERT INTO portfolio (user_id, symbol, name, shares, price, total) VALUES (?, ?, ?, ?, ?, ?)",
                           session["user_id"], symbol, name, shares, price, total)
                db.execute("INSERT INTO history (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)",
                           session["user_id"], symbol, shares, price, date)

            count = 0

        # set new remaning cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?", remainingCash, session["user_id"])

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute("SELECT * FROM history WHERE user_id = ?", session["user_id"])
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # get data
        symbol = request.form.get("symbol")
        response = lookup(symbol)
        if not symbol:
            return apology("must provide symbol", 400)
        if not response:
            return apology("must provide valid symbol", 400)

        return render_template("quoted.html", response=response)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        users = db.execute("SELECT username FROM users")
        print(password, confirmation)
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)

        elif confirmation != password:
            return apology("passwords must match", 400)

        for user in users:
            if username == user["username"]:
                return apology("username taken", 400)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username,
                   generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))
        return redirect("/", 200)

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    symbols = db.execute("SELECT symbol FROM portfolio WHERE user_id = ?", session["user_id"])
    if request.method == "POST":
        # get data
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        currentShares = db.execute("SELECT shares FROM portfolio WHERE symbol = ?", symbol)
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        response = lookup(symbol)
        price = int(response["price"])
        # calculate remaining cash
        total = price * int(shares)
        remainingCash = cash[0]["cash"] + total

        # check if the user input is correct
        if not symbol:
            return apology("must provide symbol", 400)
        if not shares:
            return apology("must provide shares", 400)
        if not shares.isdigit():
            return apology("must provide whole number", 400)
        if int(currentShares[0]["shares"]) < int(shares):
            return apology("not enough shares", 400)

        # update remaining cash and shares and add the transaction to history
        db.execute("UPDATE portfolio SET shares = shares - ? WHERE user_id = ? AND symbol = ?", shares, session["user_id"], symbol)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", remainingCash, session["user_id"])
        db.execute("DELETE FROM portfolio WHERE shares = 0 AND user_id = ?", session["user_id"])
        db.execute("INSERT INTO history (user_id, symbol, shares, price, date) VALUES (?, ?, -?, ?, ?)",
                   session["user_id"], symbol, shares, price, date)

        return redirect("/")
    else:
        return render_template("sell.html", symbols=symbols)
