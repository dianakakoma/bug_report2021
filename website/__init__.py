from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

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

    #run the function to create the database
    create_database(app)

    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #how to load a user with a primary key
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

#check if the database has already been created, if not create it. 
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
    else:
        print('Database already exists.')