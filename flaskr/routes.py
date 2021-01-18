from app import app
from flask import render_template, redirect, url_for, request, session
from users import login_user, create_user


@app.route("/")
def index():
    if "user" in session:
        render_template("index.html")
        username = session["user"]
        return render_template("index.html", username=username)
    else:
        return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        log_in_error = login_user(username, password)
        print(log_in_error)
        if log_in_error is None:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", log_in_error=log_in_error)
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
