from app.mod_auth.models import User
from app import db
import bcrypt


def login_user(username, password):
    user_found = User.query.filter_by(username=username).first()
    if not user_found:
        return "Username not found."
    else:
        if not bcrypt.checkpw(password, user_found.password):
            return "password is incorrect."
        return None


def create_user(username, email, password, repeat_password):
    username_error = username_format(username)
    password_error = password_format(password, repeat_password)
    errordict = {
            "username": username_error,
            "password": password_error
    }
    if not username_error and not password_error:    
        hashpw = bcrypt.hashpw(password, bcrypt.gensalt())
        user = User(username=username, password=hashpw, email=email)
        db.session.add(user)
        db.session.commit()
    return errordict


def username_format(username):
    errors = []
    if username.isspace() or not username:
        errors.append("Username cannot have a space character or be empty.")
    if (len(username) > 24):
        errors.append("Maximum length is 24")
    else:
        q = db.session.query(User.id).filter_by(username=username).scalar()
        if q is not None:
            errors.append("Username is taken.")
    return errors


def password_format(password, repeat_password):
    errors = []
    if (len(password) < 8):
        errors.append("Minimum length is 8.")
    if (len(password) > 24):
        errors.append("Maximum length is 24")
    if (password != repeat_password):
        errors.append("Those passwords didn't match.")
    return errors
