from app import db


class Base(db.Model):

    __abstract__ = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class Company(Base):

    __tablename__ = "companies"

   name = db.Column(db.String(100), unique=True, nullable=False)
   company_id = db.Column(db.String(15), unique=True, nullable=False)
   country = db.Column(db.String(50), nullable=False)
   street_name = db.Column(db.String(50), nullable=False)
   city = db.Column(db.String(50), nullable=False)
   postal_code = db.Column(db.String(50), nullable=False)
