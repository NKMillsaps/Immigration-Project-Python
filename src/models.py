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
            "dayPhone": self.dayPhone,
            "mobile": self.mobile,
            "application": application,
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
    dayPhone = db.Column(db.String(20), nullable=True)
    mobile = db.Column(db.String(20), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "middlename": self.middlename,
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

    def serialize(self):
        return {
            "id": self.id,
            "forms_name": self.forms_name
}