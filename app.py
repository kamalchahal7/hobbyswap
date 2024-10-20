from flask_cors import CORS
from cs50 import SQL
from flask import Flask, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functions import login_required
from db.init import create_or_init_sqlite_database

from datetime import datetime
import pytz

import re

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

utc_time = datetime.now(pytz.timezone("UTC"))
est_time = utc_time.astimezone(pytz.timezone("US/Eastern"))

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

create_or_init_sqlite_database("app.db")
db = SQL("sqlite:///app.db")


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
    """Home Route"""
    return jsonify({"message": "Welcome to the home page!"})


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login Route"""

    # error checking for received data
    if not request.is_json:
        return jsonify({"error": "Content type is not supported."}), 415

    # error checking for received json data
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # error checking for identifier
    email = data.get("email")
    if not email:
        return jsonify({"error": "Email is missing"}), 400

    # error checking for password
    password = data.get("password")
    if not password:
        return jsonify({"error": "Password missing."}), 400

    # error checking for queried account
    account = db.execute(
        "SELECT * FROM users WHERE email = ?",
        email,
    )
    if not account:
        return jsonify({"error": "Email is not registered."}), 400

    # error checking
    if len(account) != 1 or not check_password_hash(
        account[0]["password_hash"], password
    ):
        return jsonify({"error": "Pasword is incorrect."}), 400

    # intializes user_id into the session
    session["user_id"] = account[0]["id"]

    return jsonify(
        {
            "message": "Login successful!",
            "user_id": session["user_id"],
            "first_name": account[0]["first_name"],
            "last_name": account[0]["last_name"],
            "email": account[0]["email"],
        }
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    """Registration Route"""

    # error checking for received data
    if not request.is_json:
        return jsonify({"error": "Content type is not supported."}), 415

    # error checking for received json data
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # error checking for incomplete name fields
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    if not first_name or not last_name:
        return jsonify({"error": "Full name not provided."}), 400

    # error checking for birthdate
    date_of_birth = data.get("date_of_birth")
    if not date_of_birth:
        return jsonify({"error": "Date of birth not provided."}), 400

    # error checking for email
    email = data.get("email")
    if not email:
        return jsonify({"error": "Email not provided."}), 400
    if not re.match(pattern, email):
        return jsonify({"error": "Not a valid email."}), 400
    existing_emails = db.execute("SELECT email FROM users WHERE email = ?", email)
    if len(existing_emails) > 0:
        return jsonify({"error": "Email already registered."}), 400

    # error checking for password
    password = data.get("password")
    if not password:
        return jsonify({"error": "Password missing."}), 400

    # error checking for confirmation
    confirmation = data.get("confirmation")
    if not confirmation:
        return jsonify({"error": "Confirmation missing."}), 400
    if not confirmation == password:
        return jsonify({"error": "Confirmation does not match password."}), 400

    # generate password hash
    password = generate_password_hash(password)

    db.execute(
        """INSERT INTO users (email, password_hash, first_name, last_name, date_of_birth)
                VALUES (?, ?, ?, ?, ?)""",
        email,
        password,
        first_name,
        last_name,
        date_of_birth,
    )

    return jsonify({"message": "Registration successful!"})


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    return jsonify({"message": "Logout successful!"})
