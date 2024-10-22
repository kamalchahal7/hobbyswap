import os

from flask_cors import CORS
from cs50 import SQL
from flask import Flask, flash, redirect, jsonify, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

from datetime import datetime
import pytz

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return jsonify({"error": "Please log in and try again"}), 401
        return f(*args, **kwargs)

    return decorated_function
