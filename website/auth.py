from flask import Blueprint, render_template,request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template("home.html", text="testing")

@auth.route('/login', methods=["GET","POST"])
def login():
    data = request.form
    print(data) #gives us the data submitted on th form
    return render_template("login.html", text="testing")

@auth.route('/logout')
def logout():
    return "<p>You are logged out!</p>"

@auth.route('/sign-up', methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #form input restrictions
        if len(email) < 10:
            flash("email must be greater than 2 characters", category="error")
        elif len(firstName) < 2:
            flash("Your first name must be greater than 2 characters", category="error")
        elif password1 != password2:
            flash("The password confirmation does not match the initial password", category="error")
        elif len(password1) < 5:
            flash("Your password must be greater than 2 characters", category="error")
            pass
        else:
            flash("Account created!", 'success')

    return render_template("sign_up.html")