from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    #user is reporting a great idea or a bug
    bugOrIdea = db.Column(db.String(10))
    description = db.Column(db.String(300))
    suggestFix = db.Column(db.String(300))
    url = db.Column(db.String(150))
    screenshot = db.Column(db.String(150))

    #what is the status of the report? (submitted, under review, in rejected)
    status = db.Column(db.String(25))
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #associating a report's relationship with a single existing user through a foreign key. One user (parent) may have many reports (children). One to many relationship.

#user template
class User(db.Model, UserMixin):
    #define database column
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))

    #reports field allows every report to be associated with particular use so you can all the the reports of a user.
    reports = db.relationship('Note')
