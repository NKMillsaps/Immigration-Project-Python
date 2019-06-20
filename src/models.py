from flask_sqlalchemy import SQLAlchemy

# from SQLAlchemy import relationship, ForeignKey
# from flask_sqlalchemy import

# from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy.ext.declarative import SQLalchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = "person"
    spouse = db.relationship("Spouse", uselist=False, back_populates="person")
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=False, nullable=True)
    firstname = db.Column(db.String(120), unique=False, nullable=True)
    middlename = db.Column(db.String(120), unique=False, nullable=True)
    sex = db.Column(db.String(6), unique=False, nullable=True)
    dateOfBirth = db.Column(db.Date, unique=False, nullable=True)
    countryOfBirth = db.Column(db.String(30), unique=False, nullable=True)
    citizenship = db.Column(db.String(30), unique=False, nullable=True)
    US_Address = db.Column(db.String(120), unique=False, nullable=True)
    apartment = db.Column(db.String(120), unique=False, nullable=True)
    city = db.Column(db.String(30), unique=False, nullable=True)
    state = db.Column(db.String(20), unique=False, nullable=True)
    zip = db.Column(db.String(10), unique=False, nullable=True)
    mobile = db.Column(db.String(20), unique=False, nullable=True)
    spouse_id = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.person_id

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
    person = db.relationship("Person", back_populates="spouse")
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=False, nullable=True)
    firstname = db.Column(db.String(120), unique=False, nullable=True)
    middlename = db.Column(db.String(120), unique=False, nullable=True)
    sex = db.Column(db.String(6), unique=False, nullable=True)
    dateOfBirth = db.Column(db.Date, unique=False, nullable=True)
    countryOfBirth = db.Column(db.String(30), unique=False, nullable=True)
    citizenship = db.Column(db.String(30), unique=False, nullable=True)
    US_Address = db.Column(db.String(120), unique=False, nullable=True)
    apartment = db.Column(db.String(120), unique=False, nullable=True)
    city = db.Column(db.String(30), unique=False, nullable=True)
    state = db.Column(db.String(20), unique=False, nullable=True)
    zip = db.Column(db.String(10), unique=False, nullable=True)
    mobile = db.Column(db.String(20), unique=False, nullable=True)

    def __repr__(self):
        return '<Spouse %r>' % self.spouse_id

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
    children = db.relationship("Forms")
    application_name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self): return '<Application %r>' % self.application_id

    def serialize(self):
        return {
            "id": self.id,
            "application_name": self.application_name
        }

class Forms(db.Model):
    __tablename__ = "forms"
    id = db.Column(db.Integer, primary_key=True)

    application_id = db.Column(db.Integer, db.ForeignKey("application.id"))
    forms_name = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self): return '<Forms %r>' % self.forms_id

    def serialize(self):
        return {
            "id": self.id,
            "forms_name": self.forms_name
        }
