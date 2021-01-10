from app import app
from flask import render_template, redirect, request, session, url_for

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        return redirect(url_for("index"))
    else: 
        return render_template("login.html")  

@app.route("/create_user")
def create_user():
    return render_template("newUser.html")
