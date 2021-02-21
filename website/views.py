from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
#now you cannot view the homepage unless you are logged in
def home():
    return render_template("home.html",user=current_user)