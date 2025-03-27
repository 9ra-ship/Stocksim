from flask import Flask, redirect, render_template, session, g, url_for
from flask_debugtoolbar import DebugToolbarExtension
from config import Config
from db import db, connect_db
from users.models import User
from users.routes import users
from trades.routes import trades
from watchlists.routes import watchlists
from auth.routes import auth
from utils import add_user_to_session, homepage_view, request_header
from auth.login import CURR_USER_KEY
from flask import render_template

# Create Flask App
app = Flask(__name__)
app.app_context().push()
app.config.from_object(Config)

# Connect to database
connect_db(app)

# Enable DTE
debug = DebugToolbarExtension(app)

# Blueprints
app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(trades, url_prefix="/trades")
app.register_blueprint(watchlists, url_prefix="/watchlists")
app.register_blueprint(auth, url_prefix="/auth")

# @app.route('/')  # Root route
@app.route('/index.html')  # Explicit route for index.html
def lectures():
    return render_template('index.html')

@app.route('/lesson/<int:lesson_number>')
def lesson(lesson_number):
    return render_template(f'lesson{lesson_number}.html')

@app.route('/quiz/<int:quiz_number>')
def quiz(quiz_number):
    return render_template(f'quiz{quiz_number}.html')
@app.route('/progress')
def progress():
    return render_template('progress.html')
   

# Run before each request
@app.before_request
def add_user_to_g():
    """If logged in, add user to Flask global (g)"""

    add_user_to_session()

# Root view
@app.route("/")
def show_homepage():
    """Show home page view depending on user login status"""

    return homepage_view()

@app.after_request
def add_header(req):
    """Add non-caching headers on every request."""

    return request_header(req=req)

@app.errorhandler(404)
def page_not_found(e):
    """404 page"""

    return render_template("404.html"), 404



