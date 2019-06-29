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
    zipCode = db.Column(db.String(120), nullable=True)
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
            "zipCode": self.zipCode,
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
    spouseEmail = db.Column(db.String(120), unique=True, nullable=False)
    spouseLastname = db.Column(db.String(120), nullable=True)
    spouseFirstname = db.Column(db.String(120), nullable=True)
    spouseMiddlename = db.Column(db.String(120), nullable=True)
    spouseAddress = db.Column(db.String(120), nullable=True)
    spouseApartment = db.Column(db.String(120), nullable=True)
    spouseCity = db.Column(db.String(120), nullable=True)
    spouseState = db.Column(db.String(120), nullable=True)
    spouseZipCode = db.Column(db.String(120), nullable=True)
    spouseCountry = db.Column(db.String(120), nullable=True)
    spouseDayPhone = db.Column(db.String(20), nullable=True)
    spouseMobile = db.Column(db.String(20), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "spouseEmail": self.spouseEmail,
            "spouseLastname": self.spouseLastname,
            "spouseFirstname": self.spouseFirstname,
            "spouseMiddlename": self.spouseMiddlename,
            "spouseAddress": self.spouseAddress,
            "spouseApartment": self.spouseApartment,
            "spouseCity": self.spouseCity,
            "spouseState": self.spouseState,
            "spouseZipCode": self.spouseZipCode,
            "spouseCountry": self.spouseCountry,
            "spouseDayPhone": self.spouseDayPhone,
            "spouseMobile": self.spouseMobile
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
    zipCode = db.Column(db.String(120), nullable=True)
    country = db.Column(db.String(120), nullable=True)
    spouseEmail = db.Column(db.String(120), unique=True, nullable=False)
    spouseLastname = db.Column(db.String(120), nullable=True)
    spouseFirstname = db.Column(db.String(120), nullable=True)
    spouseMiddlename = db.Column(db.String(120), nullable=True)
    spouseAddress = db.Column(db.String(120), nullable=True)
    spouseApartment = db.Column(db.String(120), nullable=True)
    spouseCity = db.Column(db.String(120), nullable=True)
    spouseState = db.Column(db.String(120), nullable=True)
    spouseZipCode = db.Column(db.String(120), nullable=True)
    spouseCountry = db.Column(db.String(120), nullable=True)
    spouseDayPhone = db.Column(db.String(20), nullable=True)
    spouseMobile = db.Column(db.String(20), nullable=True)
    employerName = db.Column(db.String(120), nullable=True)
    employerAddress = db.Column(db.String(120), nullable=True)
    employerApartment = db.Column(db.String(120), nullable=True)
    employerCity = db.Column(db.String(120), nullable=True)
    employerState = db.Column(db.String(120), nullable=True)
    employerZipCode = db.Column(db.String(120), nullable=True)
    employerDayPhone = db.Column(db.String(12), nullable=True)
    employerCountry = db.Column(db.String(120), nullable=True)
    employerOccupation = db.Column(db.String(120), nullable=True)

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
            "spouseEmail": self.spouseEmail,
            "spouseLastname": self.spouseLastname,
            "spouseFirstname": self.spouseFirstname,
            "spouseMiddlename": self.spouseMiddlename,
            "spouseAddress": self.spouseAddress,
            "spouseApartment": self.spouseApartment,
            "spouseCity": self.spouseCity,
            "spouseState": self.spouseState,
            "spouseZipCode": self.spouseZipCode,
            "spouseCountry": self.spouseCountry,
            "spouseDayPhone": self.spouseDayPhone,
            "spouseMobile": self.spouseMobile,
            "employerName": self.employerName,
            "employerAddress": self.employerAddress,
            "employerApartment": self.employerApartment,
            "employerCity": self.employerCity,
            "employerState": self.employerState,
            "employerZipCode": self.employerZipCode,
            "employerDayPhone": self.employerDayPhone,
            "employerCountry": self.employerCountry,
            "employerOccupation": self.employerOccupation
}