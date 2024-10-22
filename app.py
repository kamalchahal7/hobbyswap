from flask_cors import CORS
from cs50 import SQL
from flask import Flask, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from db.init import create_or_init_sqlite_database
from functions import login_required

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

# CRUD LISTINGS ROUTE

# creating listings
@app.route("/listings", methods=["POST"])
@login_required
def create_listing():
    # error checking for received data
    if not request.is_json:
        return jsonify({"error": "Content type is not supported."}), 415

    # error checking for received json data
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # error checking if the required fields are present in the json data
    if 'title' not in data or 'description' not in data or 'condition' not in data or 'looking_for' not in data:
        return jsonify({"error": "Required fields are missing"}), 400

    # inserts the new listing into the listings table
    db.execute(
        "INSERT INTO listings (title, description, owner, condition, looking_for) VALUES (?, ?, ?, ?, ?)",
        data['title'],
        data['description'],
        session["user_id"],
        data['condition'],
        data['looking_for']
    )

    try:
        listing = db.execute("SELECT * FROM listings WHERE owner = ? AND title = ? ORDER BY date_posted DESC", session["user_id"], data['title'])[0]
        return jsonify(listing), 201
    except IndexError:
        return jsonify({"error": "We ran into an unknown error when saving your listing."}), 500


# fetching listings
@app.route("/listings", methods=["GET"])
@login_required
def get_listings():
    listings = db.execute("SELECT * FROM listings")

    return jsonify(listings), 200

# fetching a single listing
@app.route("/listings/<int:listing_id>", methods=["GET"])
@login_required
def get_listing(listing_id):
    listing = db.execute("SELECT * FROM listings WHERE id = ?", listing_id)
    if not listing:
        return jsonify({"error": "Listing not found"}), 404

    return jsonify(listing), 200

# updating listings
@app.route("/listings/<int:listing_id>", methods=["PUT"])
@login_required
def update_listing(listing_id):
    # error checking for received data
    if not request.is_json:
        return jsonify({"error": "Content type is not supported."}), 415

    # error checking for received json data
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # error checking if 'title' and 'descriptions' fields are present in the json data
    if 'title' not in data or 'description' not in data:
        return jsonify({"error": "Title and description fields are required"}), 400

    # checks if the listing exists
    listing = db.execute("SELECT * FROM listings WHERE id = ?", listing_id)
    if not listing:
        return jsonify({"error": "Listing not found"}), 404

    # update the listing's title and description
    db.execute(
        "UPDATE listings SET title = ?, description = ? WHERE id = ?",
        data['title'],
        data['description'],
        listing_id
    )

    return jsonify({"message": "Listing updated successfully!"}), 200

# deleting listings
@app.route("/listings/<int:listing_id>", methods=["DELETE"])
@login_required
def delete_listing(listing_id):
    # checks if the listing exists
    listing = db.execute("SELECT * FROM listings WHERE id = ?", listing_id)
    if not listing:
        return jsonify({"error": "Listing not found"}), 404

    # deletes the listing
    db.execute("DELETE FROM listings WHERE id = ?", listing_id)

    return jsonify({"message": "Listing deleted successfully!"}), 200

# CRUD COMMENTS ROUTE

# creating new comments
@app.route("/listings/<int:listing_id>/comments", methods=["POST"])
@login_required
def create_comment(listing_id):
    # error checking for received data
    if not request.is_json:
        return jsonify({"error": "Content type is not supported."}), 415

    # error checking for received json data
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # error checking if the fields are present in the JSON data
    if 'text' not in data or 'owner' not in data:
        return jsonify({"error": "Required fields are missing"}), 400

    # inserts the new comment into the comments table
    db.execute(
        "INSERT INTO comments (text, owner, listing, reply_to) VALUES (?, ?, ?, ?)",
        data['text'],
        data['owner'],
        listing_id,
        data.get('reply_to')  # optional field, defaults to None if not provided
    )

    return jsonify({"message": "Comment created successfully!"}), 201

# fetching comments
@app.route('/listings/<int:listing_id>/comments', methods=['GET'])
@login_required
def get_comments(listing_id):
    comments = db.execute("SELECT * FROM comments WHERE listing = ?", listing_id)
    return jsonify(comments), 200

# updating comments
@app.route("/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    # error checking for received data
    if not request.is_json:
        return jsonify({"error": "Content type is not supported."}), 415

    # error checking for received json data
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # error checking if 'text' field is present in the JSON body
    if 'text' not in data:
        return jsonify({"error": "'text' field is missing"}), 400

    # checks if the comment exists
    comment = db.execute("SELECT * FROM comments WHERE id = ?", comment_id)
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    # updates the comment's text
    db.execute("UPDATE comments SET text = ? WHERE id = ?", data['text'], comment_id)

    return jsonify({"message": "Comment updated successfully!"}), 200

# deleting comments
@app.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    # checks if the comment exists
    comment = db.execute("SELECT * FROM comments WHERE id = ?", comment_id)
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    # deletes the comment
    db.execute("DELETE FROM comments WHERE id = ?", comment_id)

    return jsonify({"message": "Comment deleted successfully!"}), 200

# CRUD TAGS ROUTE

# creating tags
@app.route("/tags", methods=["POST"])
def create_tag():
    # error checking for received data
    if not request.is_json:
        return jsonify({"error": "Content type is not supported."}), 415

    # error checking for received json data
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # error checking if the 'value' field is present
    if 'value' not in data:
        return jsonify({"error": "'value' field is required"}), 400

    # inserts the new tag into the tags table
    db.execute("INSERT INTO tags (value) VALUES (?)", data['value'])

    return jsonify({"message": "Tag created successfully!"}), 201

# fetching tags
@app.route("/tags", methods=["GET"])
def get_tags():
    tags = db.execute("SELECT * FROM tags")
    return jsonify(tags), 200

# updating tags
@app.route("/tags/<int:tag_id>", methods=["PUT"])
def update_tag(tag_id):
    # error checking for received data
    if not request.is_json:
        return jsonify({"error": "Content type is not supported."}), 415

    # error checking for received json data
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # error checking if 'value' field is present
    if 'value' not in data:
        return jsonify({"error": "'value' field is required"}), 400

    # checks if the tag exists
    tag = db.execute("SELECT * FROM tags WHERE id = ?", tag_id)
    if not tag:
        return jsonify({"value": "Tag not found"}), 404

    # updates the tag's value
    db.execute("UPDATE tags SET value = ? WHERE id = ?", data['value'], tag_id)

    return jsonify({"message": "Tag updated successfully!"}), 200

# deleting tags
@app.route("/tags/<int:tag_id>", methods=["DELETE"])
def delete_tag(tag_id):
    # checks if the tag exists
    tag = db.execute("SELECT * FROM tags WHERE id = ?", tag_id)
    if not tag:
        return jsonify({"error": "Tag not found"}), 404

    # deletes the tag
    db.execute("DELETE FROM tags WHERE id = ?", tag_id)

    return jsonify({"message": "Tag deleted successfully!"}), 200

# CRUD CATEGORIES ROUTE

# creating categories
@app.route("/categories", methods=["POST"])
def create_category():
    # error checking for received data
    if not request.is_json:
        return jsonify({"error": "Content type is not supported."}), 415

    # error checking for received json data
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # error checking if the 'title' field is present
    if 'title' not in data:
        return jsonify({"error": "'title' field is required"}), 400

    # inserts the new category into the categories table
    db.execute("INSERT INTO categories (title) VALUES (?)", data['title'])

    return jsonify({"message": "Category created successfully!"}), 201

# fetching categories
@app.route("/categories", methods=["GET"])
def get_categories():
    categories = db.execute("SELECT * FROM categories")
    return jsonify(categories), 200

# updating categories
@app.route("/categories/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    # error checking for received data
    if not request.is_json:
        return jsonify({"error": "Content type is not supported."}), 415

    # error checking for received json data
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # error checking if 'title' field is present
    if 'title' not in data:
        return jsonify({"error": "'title' field is required"}), 400

    # checks if the category exists
    category = db.execute("SELECT * FROM categories WHERE id = ?", category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404

    # update the category's title
    db.execute("UPDATE categories SET title = ? WHERE id = ?", data['title'], category_id)

    return jsonify({"message": "Category updated successfully!"}), 200

# deleting categories
@app.route("/categories/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    # checks if the category exists
    category = db.execute("SELECT * FROM categories WHERE id = ?", category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404

    # deletes the category
    db.execute("DELETE FROM categories WHERE id = ?", category_id)

    return jsonify({"message": "Category deleted successfully!"}), 200
