from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class CompanyForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    company_id = StringField("Company Id", validators=[InputRequired()])
    country = StringField("Country", validators=[InputRequired()])
    street_name = StringField("Street Name", validators=[InputRequired()])
    city = StringField("City", validators=[InputRequired()])
    postal_code = StringField("Postal Code", validators=[InputRequired()])
    submit = SubmitField("Submit")
