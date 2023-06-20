from . import db
from flask_login import UserMixin
from sqlalchemy import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    texts = db.relationship('Text')


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rawText = db.Column(db.String(2000))
    keywords = db.Column(db.String(600))
    tags = db.Column(db.String(600))
    sentiment = db.Column(db.Float)
    wordCount = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
