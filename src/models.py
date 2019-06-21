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
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), nullable=True)
    firstname = db.Column(db.String(120), nullable=True)
    middlename = db.Column(db.String(120), nullable=True)
    sex = db.Column(db.String(6), nullable=True)
    dateOfBirth = db.Column(db.DateTime, nullable=True)
    countryOfBirth = db.Column(db.String(30))
    citizenship = db.Column(db.String(30), unique=False, nullable=True)
    US_Address = db.Column(db.String(120), unique=False, nullable=True)
    apartment = db.Column(db.String(120), unique=False, nullable=True)
    city = db.Column(db.String(30), unique=False, nullable=True)
    state = db.Column(db.String(20), unique=False, nullable=True)
    zip = db.Column(db.String(10), unique=False, nullable=True)
    mobile = db.Column(db.String(20), unique=False, nullable=True)
    #spouse_id = db.Column(db.Integer, unique=True, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "sex": self.sex,
            "dateOfBirth": self.dateOfBirth,
            "countryOfBirth": self.countryOfBirth,
            "citizenship": self.citizenship,
            "US_Address": self.US_Address,
            "apartment": self.apartment,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "mobile": self.mobile
        }

class Spouse(db.Model):
    __tablename__ = 'spouse'
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    # person = db.relationship("Person", back_populates="spouse")
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=False, nullable=True)
    firstname = db.Column(db.String(120), unique=False, nullable=True)
    middlename = db.Column(db.String(120), unique=False, nullable=True)
    sex = db.Column(db.String(6), unique=False, nullable=True)
    dateOfBirth = db.Column(db.DateTime, unique=False, nullable=True)
    countryOfBirth = db.Column(db.String(30), unique=False, nullable=True)
    citizenship = db.Column(db.String(30), unique=False, nullable=True)
    US_Address = db.Column(db.String(120), unique=False, nullable=True)
    apartment = db.Column(db.String(120), unique=False, nullable=True)
    city = db.Column(db.String(30), unique=False, nullable=True)
    state = db.Column(db.String(20), unique=False, nullable=True)
    zip = db.Column(db.String(10), unique=False, nullable=True)
    mobile = db.Column(db.String(20), unique=False, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "sex": self.sex,
            "dateOfBirth": self.dateOfBirth,
            "countryOfBirth": self.countryOfBirth,
            "citizenship": self.citizenship,
            "US_Address": self.US_Address,
            "apartment": self.apartment,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "mobile": self.mobile
        }

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    application_name = db.Column(db.String(80), unique=True, nullable=False)
    forms = db.relationship("Forms")

    def serialize(self):
        return {
            "id": self.id,
            "application_name": self.application_name
        }

class Forms(db.Model):
    __tablename__ = "forms"
    id = db.Column(db.Integer, primary_key=True)
    forms_name = db.Column(db.String(120), unique=False, nullable=False)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'))

    def serialize(self):
        return {
            "id": self.id,
            "forms_name": self.forms_name
        }
