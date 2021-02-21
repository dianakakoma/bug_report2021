from flask import Blueprint, render_template,request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template("home.html", text="testing")

@auth.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        #query/search the database to confirm the the person trying to login has actually sign-up and return the first result
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                #user remains login until webserver session is interrupted in some way.
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("The email entered does not exist in our records, try again.", category="error")
    return render_template("login.html",user=current_user)

@auth.route('/logout')
@login_required
#now you cannot logout unless you are logged in
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/sign-up', methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("this user already exists", category="error")
        #form input restrictions
        elif len(email) < 10:
            flash("email must be greater than 2 characters", category="error")
        elif len(firstName) < 2:
            flash("Your first name must be greater than 2 characters", category="error")
        elif password1 != password2:
            flash("The password confirmation does not match the initial password", category="error")
        elif len(password1) < 5:
            flash("Your password must be greater than 2 characters", category="error")
            pass
        else:
            new_user = User(email=email, firstName=firstName,
            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created! Awesome!", 'success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)