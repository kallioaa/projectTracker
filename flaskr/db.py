from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


# Or models: User table


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), nullable=False)

class comppany(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comppany_name = db.Column(db.String(50), unique=True, nullable=False)
    comppany_id = db.Column(db.String(10), unique=True, nullable=False)


db.create_all()
