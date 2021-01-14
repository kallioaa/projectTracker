from app import app
from flask import render_template, request
from users import login_user, create_user


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        login_user(username, password)
        return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/newUser", methods=["POST", "GET"])
def new_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        password_repeat = request.form["password_repeat"]
        status_info = create_user(username, email, password, password_repeat)
        username_error = '\n'.join(status_info["username"])
        password_error = '\n'.join(status_info["password"])
        return render_template("newUser.html", username_error=username_error, password_error=password_error)
    else:
        return render_template("newUser.html")
