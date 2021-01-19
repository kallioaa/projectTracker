from app import app
from flask import render_template, redirect, url_for, request, session, Blueprint
from app.mod_auth.usermodel import login_user, create_user


mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        log_in_error = login_user(username, password)
        print(log_in_error)
        if log_in_error is None:
            session["user"] = username
            return "<p> kirjauduttu <p>"
        return render_template("auth/login.html", log_in_error=log_in_error)
    return render_template("auth/login.html")


@mod_auth.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        password_repeat = request.form["password_repeat"]
        status_info = create_user(username, email, password, password_repeat)
        username_error = '\n'.join(status_info["username"])
        password_error = '\n'.join(status_info["password"])
        return render_template("auth/new_user.html", username_error=username_error, password_error=password_error)
    return render_template("auth/new_user.html")
