import os

from flask_cors import CORS
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functions import login_required

from datetime import datetime
import pytz

import re
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

utc_time = datetime.now(pytz.timezone('UTC'))
est_time = utc_time.astimezone(pytz.timezone('US/Eastern'))

app = Flask(__name__)
CORS(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///users.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method=="GET":
        return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        # error checking for identifier 
        identifier = request.form.get("identifier")
        if not identifier:
            mssg = "Username/Email is missing"
            return redirect(url_for('error', error=mssg))

        # error checking for password
        password = request.form.get("password")
        if not password:
            mssg= "Password missing."
            return redirect(url_for('error', error=mssg))

        # error checking for queried account
        account = db.execute("SELECT * FROM users WHERE username = ? OR email = ?", identifier, identifier)
        if not account:
            mssg = "Username/Email is not registered."
            return redirect(url_for('error', error=mssg))

        # error checking 
        if len(account) != 1 or not check_password_hash(
            account[0]["password_hash"], password):
            mssg = "Pasword is incorrect."
            return redirect(url_for('error', error=mssg))
        
        # intializes user_id into the session
        session["user_id"] = account[0]['id']

        # redirects to home
        return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        # error checking for incomplete name fields
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        if not first_name or not last_name:
            mssg = "Full name not provided."
            return redirect(url_for('error', error=mssg))
        
        # error checking for birthdate
        date_of_birth = request.form.get("date_of_birth")
        if not date_of_birth:
            mssg = "Date of birth not provided."
            return redirect(url_for('error', error=mssg))
        
        # error checking for email
        email = request.form.get("email")
        if not email:
            mssg = "Email not provided."
            return redirect(url_for('error', error=mssg))
        if not re.match(pattern, email):
            mssg = "Not a valid email."
            return redirect(url_for('error', error=mssg))
        existing_emails = db.execute("SELECT email FROM users")
        for existing_email in existing_emails:
            if email == existing_email['email']:
                mssg = "Email already registered."
                return redirect(url_for('error', error=mssg))

        # error checking for username
        username = request.form.get("username")
        if not username:
            mssg = "Username not provided."
            return redirect(url_for('error', error=mssg))
        existing_usernames = db.execute("SELECT username FROM users")
        for existing_username in existing_usernames:
            if username == existing_username['username']:
                mssg = "Username already registered."
                return redirect(url_for('error', error=mssg))

        # error checking for password
        password = request.form.get("password")
        if not password:
            mssg = "Password missing."
            return redirect(url_for('error', error=mssg))

        # error checking for confirmation
        confirmation = request.form.get("confirmation")
        if not confirmation:
            mssg = "Confirmation missing."
            return redirect(url_for('error', error=mssg))
        if not confirmation == password:
            mssg = "Confirmation does not match password."
            return redirect(url_for('error', error=mssg))
        
        # generate password hash
        password = generate_password_hash(password)

        db.execute("""INSERT INTO users (username, password_hash, email, first_name, last_name, date_of_birth)
                    VALUES (?, ?, ?, ?, ?, ?)""", username, password, email, first_name, last_name, date_of_birth)

        return redirect("/login")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/error", methods=["GET"])
def error():
    if request.method=="GET":
        error = request.args.get("error")
        return render_template("error.html", error=error)