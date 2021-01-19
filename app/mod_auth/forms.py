from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(), Length(min=1, max=25)])
    password = PasswordField("password", validators=[InputRequired(), Length(min=8, max=60)])
    submit = SubmitField('Submit')


class CreateUserForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(), Length(message="length if off ",min=1, max=25)])
    password = PasswordField("password", validators=[InputRequired(), Length(min=8, max=60)])
    password_repeat = PasswordField("password repeat", validators=[InputRequired(), EqualTo("password")])
    email = StringField("email", validators=[InputRequired(), Email()])
    submit = SubmitField('Submit')
