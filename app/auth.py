from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import User
from config import Config

auth_bp = Blueprint('auth', __name__)

# Initialize Flask-Login and Bcrypt
login_manager = LoginManager()
bcrypt = Bcrypt()

# TODO: Replace with a real DB for a scalable system
# Simulated user data in dict
USERS = {
    Config.SYSTEM_USERNAME: User(Config.SYSTEM_USERNAME)
}

PASSWORD_HASH = generate_password_hash(Config.SYSTEM_PASSWORD)


@login_manager.user_loader
def load_user(user_id):
    return USERS.get(user_id)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and check_password_hash(PASSWORD_HASH, password):
            user = USERS[username]
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'error')

    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('auth.login'))
