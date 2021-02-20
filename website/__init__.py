from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

#initialize Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret key"
    app.config['SQLALCHEMY_DATABASE_URI']= f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #import the User and Report Models
    from .models import User, Report

    return app

#check database has been created yet, if not create it. 
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create.all(app=app)
        Print('Created Database!')