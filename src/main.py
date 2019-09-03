"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from flask_jwt_simple import (
    JWTManager, jwt_required, create_jwt, get_jwt_identity
)
from models import db, Person, Spouse, Application, Forms

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Setup the Flask-JWT-Simple extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    params = request.get_json()
    username = params.get('username', None)
    email = params.get('email', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400

    usercheck = Person.query.filter_by(username=username, email=email).first()
    if usercheck == None:
        return jsonify({"msg": "Bad username or email"}), 401
    # if username != 'test' or email != 'test':
    #     return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    ret = {'jwt': create_jwt(identity=username)}
    return jsonify(ret), 200


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/person', methods=['POST', 'GET'])
def handle_person():
    """
    Create person and retrieve all persons
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()
        spouse = []
        for g_g in body['spouse']:
            spouses = Spouse.query.get(g_g)
            spouse.append(spouses)

        application = []
        for a_a in body['application']:
            applications = Application.query.get(a_a)
            application.append(applications)

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if "email" not in body:
            raise APIException("You need to specify the email", status_code=400)
        if "username" not in body:
            raise APIException("You need to specify the username", status_code=400)
        if "lastname" not in body:
            raise APIException("You need to specify Last Name", status_code=400)
        if "firstname" not in body:
            raise APIException("You need to specify the First Name", status_code=400)
        if "middlename" not in body:
            raise APIException("You need to specify the Middle Name or N/A", status_code=400)
        if "dayPhone" not in body:
            raise APIException("You need to specify Day Phone or N/A", status_code=400)
        if "mobile" not in body:
            raise APIException("You need to specify your mobile phone number", status_code=400)
        if "lastname1" not in body:
            raise APIException("You need to specify Last Name or N/A", status_code=400)
        if "firstname1" not in body:
            raise APIException("You need to specify the First Name or N/A", status_code=400)
        if "middlename1" not in body:
            raise APIException("You need to specify the Middle Name or N/A", status_code=400)

        user1 = Person(email=body["email"], application=application, spouse=spouse, username=body["username"], lastname=body["lastname"], firstname=body["firstname"], middlename=body["middlename"], dayPhone=body["dayPhone"], mobile=body["mobile"], lastname1=body["lastname1"], firstname1=body["firstname1"], middlename1=body["middlename1"], )
        db.session.add(user1)
        db.session.commit()
        return "ok", 200
    # GET request
    if request.method == 'GET':
        all_people = Person.query.all()
        all_people = list(map(lambda x: x.serialize(), all_people))
        return jsonify(all_people), 200

    return "Invalid Method", 404

@app.route('/person/<int:person_id>', methods=['PUT', 'GET', 'DELETE'])
def get_single_person(person_id):
    """
    Single person
    """

    # PUT request
    if request.method == 'PUT':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)

        user1 = Person.query.get(person_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        if "username" in body:
            user1.username = body["username"]
        if "email" in body:
            user1.email = body["email"]
        if "address" in body:
            user1.address = body["address"]
        if "apartment" in body:
            user1.apartment = body["apartment"]
        if "city" in body:
            user1.city = body["city"]
        if "state" in body:
            user1.state = body["state"]
        if "zipCode" in body:
            user1.zipCode = body["zipCode"]
        if "country" in body:
            user1.country = body["country"]
        if "address1" in body:
            user1.address1 = body["address1"]
        if "apartment1" in body:
            user1.apartment1 = body["apartment1"]
        if "city1" in body:
            user1.city1 = body["city1"]
        if "state1" in body:
            user1.state1 = body["state1"]
        if "zipCode1" in body:
            user1.zipCode1 = body["zipCode1"]
        if "country1" in body:
            user1.country1 = body["country1"]
        if "logged_in" in body:
            user1.logged_in = body["logged_in"]

        application = []
        for a_a in body['application']:
            applications = Application.query.get(a_a)
            application.append(applications)
        if "application" in body:
            user1.application = application
        spouse = []
        for g_g in body['spouse']:
            spouses = Spouse.query.get(g_g)
            spouse.append(spouses)
        if "spouse" in body:
            user1.spouse = spouse

        db.session.commit()

        return jsonify(user1.serialize()), 200

    # GET request
    if request.method == 'GET':
        user1 = Person.query.get(person_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        return jsonify(user1.serialize()), 200

    # DELETE request
    if request.method == 'DELETE':
        user1 = Person.query.get(person_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        db.session.delete(user1)
        db.session.commit()
        return "ok", 200

    return "Invalid Method", 404

@app.route('/spouse', methods=['POST', 'GET'])
def handle_spouse():
    """
    Create spouse and retrieve all spouse
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()
        person = []


        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if "spouseEmail" not in body:
            raise APIException("You need to specify the email", status_code=400)
        if "spouseLastname" not in body:
            raise APIException("You need to specify Last Name", status_code=400)
        if "spouseFirstname" not in body:
            raise APIException("You need to specify the First Name", status_code=400)
        if "spouseMiddlename" not in body:
            raise APIException("You need to specify the Middle Name or N/A", status_code=400)
        if "spouseDayPhone" not in body:
            raise APIException("You need to specify Day Phone or N/A", status_code=400)
        if "spouseMobile" not in body:
            raise APIException("You need to specify your phone number", status_code=400)

        spouse1 = Spouse(spouseEmail=body["spouseEmail"], spouseLastname=body["spouseLastname"], spouseFirstname=body["spouseFirstname"], spouseMiddlename=body["spouseMiddlename"], spouseDayPhone=body["spouseDayPhone"], spouseMobile=body["spouseMobile"])
        db.session.add(spouse1)
        db.session.commit()
        return "ok", 200
        # return jsonify(spouse1.serialize()), 200

    # GET request
    if request.method == 'GET':
        all_spouses = Spouse.query.all()
        all_spouses = list(map(lambda x: x.serialize(), all_spouses))
        return jsonify(all_spouses), 200

    return "Invalid Method", 404

@app.route('/spouse/<int:spouse_id>', methods=['PUT', 'GET', 'DELETE'])
def get_single_spouse(spouse_id):

    """
    Single spouse
    """
    # PUT request
    if request.method == 'PUT':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)

    spouse1 = Spouse.query.get(spouse_id)
    if spouse1 is None:
        raise APIException('User not found', status_code=404)
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if "spouseEmail" in body:
        spouse1.spouseEmail = body["spouseEmail"]
    if "spouseAddress" in body:
        spouse1.spouseAddress = body["spouseAddress"]
    if "spouseApartment" in body:
        spouse1.spouseApartment = body["spouseApartment"]
    if "spouseCity" not in body:
        spouse1.spouseCity = body["spouseCity"]
    if "spouseState" not in body:
        spouse1.spouseState = body["spouseState"]
    if "spouseZipCode" not in body:
        spouse1.spouseZipCode = body["spouseZipCode"]
    if "spouseCountry" not in body:
        spouse1.spouseCountry = body["spouseCountry"]

    db.session.commit()
    return jsonify(spouse1.serialize()), 200

    # GET request
    if request.method == 'GET':
        spouse1 = Spouse.query.get(spouse_id)
        if spouse1 is None:
            raise APIException('User not found', status_code=404)
        return jsonify(spouse1.serialize()), 200

    # DELETE request
    if request.method == 'DELETE':
        spouse1 = Spouse.query.get(spouse_id)
        if spouse1 is None:
            raise APIException('Spouse not found', status_code=404)
        db.session.delete(spouse1)
        db.session.commit()
        return "ok", 200

    return "Invalid Method", 404


@app.route('/application', methods=['POST', 'GET'])
def handle_application():
    """
    Create application and retrieve all applications
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()
        forms = []
        for g_g in body['form']:
            form = Forms.query.get(g_g)
            forms.append(form)
    # if body is None:
        # raise APIException("You need to specify the request body as a json object", status_code=400)
        if "application_name" not in body:
            raise APIException("You need to specify the application", status_code=400)

        apps1 = Application(application_name=body['application_name'], forms=forms)
        db.session.add(apps1)
        db.session.commit()
        return "ok", 200

    # GET request
    if request.method == 'GET':
        all_applications = Application.query.all()
        all_applications = list(map(lambda x: x.serialize(), all_applications))
        return jsonify(all_applications), 200

    return "Invalid Method", 404


@app.route('/application/<int:application_id>', methods=['PUT', 'GET', 'DELETE'])
def get_single_application(application_id):
    """
    Single application
    """

    # PUT request
    if request.method == 'PUT':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)

        apps1 = Application.query.get(application_id)
        if apps1 is None:
            raise APIException('User not found', status_code=404)

        if "application_name" in body:
            apps1.application_name = body["application_name"]

    forms = []
    for x_x in body['forms']:
        form = Forms.query.get(x_x)
        forms.append(form)
    if "forms" in body:
        apps1.forms = forms

        db.session.commit()
        return jsonify(apps1.serialize()), 200

    # GET request
    if request.method == 'GET':
        apps1 = Application.query.get(application_id)
        if apps1 is None:
            raise APIException('Application not found', status_code=404)
        return jsonify(apps1.serialize()), 200

    # DELETE request
    if request.method == 'DELETE':
        apps1 = Application.query.get(application_id)
        if apps1 is None:
            raise APIException('Application not found', status_code=404)
        db.session.delete(apps1)
        db.session.commit()
        return "ok", 200

    return "Invalid Method", 404

@app.route('/forms', methods=['POST', 'GET'])
def handle_forms():
    """
    Create forms and retrieve all forms
    """

    # POST request
    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if "forms_name" not in body:
            raise APIException("You need to specify the forms_name", status_code=400)

        form1 = Forms(forms_name=body['forms_name'])
        db.session.add(form1)
        db.session.commit()
        return "ok", 200

    # GET request
    if request.method == 'GET':
        all_forms = Forms.query.all()
        all_forms = list(map(lambda x: x.serialize(), all_forms))
        return jsonify(all_forms), 200

    return "Invalid Method", 404

@app.route('/forms/<int:forms_id>', methods=['PUT', 'GET', 'DELETE'])
def get_single_forms(forms_id):
    """
    Single forms
    """

    # PUT request
    if request.method == 'PUT':
        body = request.get_json()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)

        form1 = Forms.query.get(forms_id)
        if form1 is None:
            raise APIException('Information not found', status_code=404)
        if "forms_name" in body:
            form1.forms_name = body["forms_name"]
        if "email" in body:
            form1.email = body["email"]
        if "lastname" in body:
            form1.lastname = body["lastname"]
        if "firstname" in body:
            form1.firstname = body["firstname"]
        if "middlename" in body:
            form1.middlename = body["middlename"]
        if "dayPhone" in body:
            form1.dayPhone = body["dayPhone"]
        if "mobile" in body:
            form1.mobile = body["mobile"]
        if "address" in body:
            form1.address = body["address"]
        if "apartment" in body:
            form1.apartment = body["apartment"]
        if "city" in body:
            form1.city = body["city"]
        if "state" in body:
            form1.state = body["state"]
        if "zipCode" in body:
            form1.zipCode = body["zipCode"]
        if "country" in body:
            form1.country = body["country"]
        if "is_completed" in body:
            form1.is_completed = body["is_completed"]
        if "spouseEmail" in body:
            form1.spouseEmail = body["spouseEmail"]
        if "spouseDayPhone" in body:
            form1.spouseDayPhone = body["spouseDayPhone"]
        if "spouseFirstname" in body:
            form1.spouseFirstname = body["spouseFirstname"]
        if "spouseLastname" in body:
            form1.spouseLastname = body["spouseLastname"]
        if "spouseMiddlename" in body:
            form1.spouseMiddlename = body["spouseMiddlename"]
        if "spouseMobile" in body:
            form1.spouseMobile = body["spouseMobile"]
        if "spouseAddress" in body:
            form1.spouseAddress = body["spouseAddress"]
        if "spouseApartment" in body:
            form1.spouseApartment = body["spouseApartment"]
        if "spouseCity" in body:
            form1.spouseCity = body["spouseCity"]
        if "spouseCountry" in body:
            form1.spouseCountry = body["spouseCountry"]
        if "spouseState" in body:
            form1.spouseMobile = body["spouseMobile"]
        if "spouseZipCode"in body:
            form1.spouseZipCope = body["spouseZipCode"]
        if "employerName" in body:
            form1.employerName = body["employerName"]
        if "employerAddress" in body:
            form1.employerAddress = body["employerAddress"]
        if "employerApartment" in body:
            form1.employerApartment = body["employerApartment"]
        if "employerCity" in body:
            form1.employerCity = body["employerCity"]
        if "employerState" in body:
            form1.employerState = body["employerState"]
        if "employerZipCode" in body:
            form1.employerZipCode = body["employerZipCode"]
        if "employerCountry" in body:
            form1.employerCountry = body["employerCountry"]
        if "employerDayPhone" in body:
            form1.employerDayPhone = body["employerDayPhone"]
        if "employerMobile" in body:
            form1.employerMobile = body["employerMobile"]

        db.session.commit()

        return jsonify(form1.serialize()), 200

    # GET request
    if request.method == 'GET':
        form1 = Forms.query.get(forms_id)
        if form1 is None:
            raise APIException('Informaion not found', status_code=404)
        return jsonify(form1.serialize()), 200

    # DELETE request
    if request.method == 'DELETE':
        form1 = Forms.query.get(forms_id)
        if form1 is None:
            raise APIException('Information not found', status_code=404)
        db.session.delete(form1)
        db.session.commit()
        return "ok", 200

    return "Invalid Method", 404


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)