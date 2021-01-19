from app import app, db
from flask import render_template, redirect, url_for, request, session, Blueprint
from app.mod_company.forms import CompanyForm

mod_company = Blueprint('company', __name__, url_prefix='/company')

@mod_company.route('/add_company', methods=['GET', 'POST'])
def add_company():
    form = CompanyForm()
    return render_template("company/add_company.html", form=form)



