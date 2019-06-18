from flask_sqlalchemy import SQLAlchemy

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
countyOfBirth = db.Column(db.String(30), unique=False, nullable=True)
citizenship = db.Column(db.String(30), unique=False, nullable=True)
US_Address = db.Column(db.String(120), unique=False, nullable=True)
apartment = db.Column(db.String(120), unique=False, nullable=True)
city = db.Column(db.String(30), unique=False, nullable=True)
state = db.Column(db.String(20), unique=False, nullable=True)
zip = db.Column(db.String(10), unique=False, nullable=True)
mobile = db.Column(db.String(20), unique=False, nullable=True)



def __repr__(self):
    return '<Person %r>' % self.person_id

def serialize(self):
    return {
        "username": self.username,
        "email": self.email,
        "lastname": self.lastname,
        "firstname": self.firstname,
        "middlename": self.middlename,
        "sex": self.sex,
        "dateOfBirth": self.dateOfBirth,
        "countyOfBirth": self.countyOfBirth,
        "citizenship": self.citizenship,
        "US_Address": self.US_Address,
        "apartment": self.apartment,
        "city": self.city,
        "state": self.state,
        "zip": self.zip,
        "mobile": self.mobile,
        "person_id": self.person_id,
        "spouse_id": self.spouse_id,
        "application_id": self.application_id

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
        countyOfBirth = db.Column(db.String(30), unique=False, nullable=True)
        citizenship = db.Column(db.String(30), unique=False, nullable=True)
        US_Address = db.Column(db.String(120), unique=False, nullable=True)
        apartment = db.Column(db.String(120), unique=False, nullable=True)
        city = db.Column(db.String(30), unique=False, nullable=True)
        state = db.Column(db.String(20), unique=False, nullable=True)
        zip = db.Column(db.String(10), unique=False, nullable=True)
        mobile = db.Column(db.String(20), unique=False, nullable=True)
        spouse_id = db.Column(db.Integer(20), unique=True, nullable=True)




    def __repr__(self):
        return '<Spouse %r>' % self.email

    def serialize(self):
        return {
            "email": self.email,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "sex": self.sex,
            "dateOfBirth": self.dateOfBirth,
            "countyOfBirth": self.countyOfBirth,
            "citizenship": self.citizenship,
            "US_Address": self.US_Address,
            "apartment": self.apartment,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "mobile": self.mobile,
        }


    class Application(db.Model):
        __tablename__ = 'application'
        id = db.Column(db.Integer, primary_key=True)
        children = db.relationship("Forms")
        application_name = db.Column(db.String(80), unique=True, nullable=False)
        application_id = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self): return '<Application %r>' % self.application.id

    def serialize(self):
        return {
            "form_done": self.form_done,
            "application_id": self.application_id
        }


    class Forms(db.Model):
        __tablename__ = "forms"
        id = db.Column(db.Integer, primary_key=True)
        application_id = db.Column(db.Integer, db.ForeignKey("application.id"))
        forms_id = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Forms %r>' % self.email

    def serialize(self):
        return { "email": self.email,  "forms_id": self.forms_id}
