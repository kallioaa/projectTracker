from app import app
from flask import render_template, redirect, url_for, request, session, Blueprint
from app.mod_auth.forms import LoginForm, CreateUserForm


mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return render_template("auth/login.html", form=form)
    return render_template("auth/login.html",form=form)


@mod_auth.route('/new_user', methods=['GET', 'POST'])
def new_user():
    form = CreateUserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        return render_template("auth/new_user.html", form=form)
    return render_template("auth/new_user.html", form=form)
