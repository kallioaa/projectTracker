from app.mod_auth.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, Email, ValidationError, StopValidation
import bcrypt


class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired()])
    submit = SubmitField("Log in", validators=[])

    # Checks if login attemps is successful
    def validate_submit(form,reduntant):
        username = form["username"]
        password = form["password"]
        user = User.query.filter_by(username=username.data).first()
        if not user:
            username.errors.append(ValidationError("Username is incorrect!"))
        else:    
            password_correct = bcrypt.checkpw(password.data,user.password)
            if not password_correct:
                password.errors.append(ValidationError("Password is incorrect!"))



class CreateUserForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(), Length(message="length if off ",min=1, max=25)])
    password = PasswordField("password", validators=[InputRequired(), Length(min=8, max=60)])
    password_repeat = PasswordField("password repeat", validators=[InputRequired(), EqualTo("password")])
    email = StringField("email", validators=[InputRequired(), Email()])
    submit = SubmitField('Create new user')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username is taken!")
        
    