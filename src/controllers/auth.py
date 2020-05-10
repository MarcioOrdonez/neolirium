from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from ..models import User
from ..app import db

module = Blueprint('auth',__name__)

@module.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@module.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))

@module.route('/signup')
def signup():
    return render_template('signup.html')

@module.route('/signup', methods=['POST'])
def signup_post():
    user_email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=user_email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = User(username=name, password=generate_password_hash(password, method='sha256'),email=user_email, admin=True)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@module.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))