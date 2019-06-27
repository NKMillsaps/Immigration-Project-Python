from flask_sqlalchemy import SQLAlchemy

# from SQLAlchemy import relationship, ForeignKey
# from flask_sqlalchemy import relationship,ForeignKey

# from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy.ext.declarative import SQLalchemy

db = SQLAlchemy()


class Person(db.Model):
    __tablename__ = "person"
    spouse = db.relationship("Spouse")
    application = db.relationship("Application")
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(120), nullable=True)
    firstname = db.Column(db.String(120), nullable=True)
    middlename = db.Column(db.String(120), nullable=True)
    dayPhone = db.Column(db.String(12), nullable=True)
    mobile = db.Column(db.String(20), nullable=True)
    logged_in = db.Column(db.Boolean(), default=False)
    address = db.Column(db.String(120), nullable=True)
    apartment = db.Column(db.String(120), nullable=True)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)
    zip_code = db.Column(db.String(120), nullable=True)
    country = db.Column(db.String(120), nullable=True)

    #spouse_id = db.Column(db.Integer, unique=True, nullable=False)


    def serialize(self):
        spouse = []
        for p in self.spouse:
            spouse.append(p.serialize())
        application = []
        for i in self.application:
            application.append(i.serialize())
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "logged_in": self.logged_in,
            "application": application,
            "address": self.address,
            "apartment": self.apartment,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "country": self.country,
            "dayPhone": self.dayPhone,
            "mobile": self.mobile,
            "spouse": spouse
        }

class Spouse(db.Model):
    __tablename__ = 'spouse'
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    # person = db.relationship("Person", back_populates="spouse")
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), nullable=True)
    firstname = db.Column(db.String(120), nullable=True)
    middlename = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    apartment = db.Column(db.String(120), nullable=True)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)
    zip_code = db.Column(db.String(120), nullable=True)
    country = db.Column(db.String(120), nullable=True)
    dayPhone = db.Column(db.String(20), nullable=True)
    mobile = db.Column(db.String(20), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "address": self.address,
            "apartment": self.apartment,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "country": self.country,
            "dayPhone": self.dayPhone,
            "mobile": self.mobile
        }

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    application_name = db.Column(db.String(80), unique=True, nullable=False)
    forms = db.relationship("Forms")



    def serialize(self):
        forms = []
        for g in self.forms:
            forms.append(g.serialize())
        return {
            "id": self.id,
            "application_name": self.application_name,
            "forms": forms
        }

class Forms(db.Model):
    __tablename__ = "forms"

    id = db.Column(db.Integer, primary_key=True)
    forms_name = db.Column(db.String(120), unique=False, nullable=False)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'))
    is_completed = db.Column(db.Boolean(), default=False)
    email = db.Column(db.String(120), nullable=True)
    lastname = db.Column(db.String(120), nullable=True)
    firstname = db.Column(db.String(120), nullable=True)
    middlename = db.Column(db.String(120), nullable=True)
    dayPhone = db.Column(db.String(12), nullable=True)
    mobile = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    apartment = db.Column(db.String(120), nullable=True)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)
    zip_code = db.Column(db.String(120), nullable=True)
    country = db.Column(db.String(120), nullable=True)
    employer_name = db.Column(db.String(120), nullable=True)
    employer_address = db.Column(db.String(120), nullable=True)
    employer_apartment = db.Column(db.String(120), nullable=True)
    employer_city = db.Column(db.String(120), nullable=True)
    employer_state = db.Column(db.String(120), nullable=True)
    employer_zip_code = db.Column(db.String(120), nullable=True)
    employer_dayPhone = db.Column(db.String(12), nullable=True)
    employer_country = db.Column(db.String(120), nullable=True)
    employer_occupation = db.Column(db.String(120), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "forms_name": self.forms_name,
            "is_completed": self.is_completed,
            "email": self.email,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "address": self.address,
            "apartment": self.apartment,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "country": self.country,
            "dayPhone": self.dayPhone,
            "mobile": self.mobile,
            "employer_name": self.employer_name,
            "employer_address": self.employer_address,
            "employer_apartment": self.employer_apartment,
            "employer_city": self.employer_city,
            "employer_state": self.employer_state,
            "employer_zip_code": self.employer_zip_code,
            "employer_dayPhone": self.employer_dayPhone,
            "employer_country": self.employer_country,
            "employer_occupation": self.employer_dayPhone,
}