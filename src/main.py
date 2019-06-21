"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Person, Spouse, Application, Forms

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

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

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)

        if "email" not in body:
            raise APIException("You need to specify the email", status_code=400)
        if "lastname" not in body:
            raise APIException("You need to specify Last Name", status_code=400)
        if "firstname" not in body:
            raise APIException("You need to specify the First Name", status_code=400)
        if "middlename" not in body:
            raise APIException("You need to specify the Middle Name or N/A", status_code=400)
        if "sex" not in body:
            raise APIException("You need to specify gender", status_code=400)
        if "dateOfBirth" not in body:
            raise APIException("You need to specify your date of birth", status_code=400)
        if "countryOfBirth" not in body:
            raise APIException("You need to specify your country of birth or N/A", status_code=400)
        if "citizenship" not in body:
            raise APIException("You need to specify your citizenship or N/A", status_code=400)
        if "US_Address" not in body:
            raise APIException("You need to specify your address", status_code=400)
        if "city" not in body:
            raise APIException("You need to specify the city", status_code=400)
        if "state" not in body:
            raise APIException("You need to specify state", status_code=400)
        if "zip" not in body:
            raise APIException("You need to specify zip code", status_code=400)
        if "mobile" not in body:
            raise APIException("You need to specify your phone number or N/A", status_code=400)

        user1 = Person(username=body["username"],email=body["email"], lastname=body["lastname"], firstname=body["firstname"], middlename=body["middlename"], sex=body["sex"], dateOfBirth=body["dateOfBirth"], countryOfBirth=body["countryOfBirth"], citizenship=body["citizenship"], US_Address=body["US_Address"], mobile=body["mobile"],apartment=body["apartment"], city=body["city"], state=body["state"], zip=body["zip"])
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
        if "lastname" not in body:
            raise APIException("You need to specify Last Name", status_code=400)
        if "firstname" not in body:
            raise APIException("You need to specify the First Name", status_code=400)
        if "middlename" not in body:
            raise APIException("You need to specify the Middle Name or N/A", status_code=400)
        if "sex" not in body:
            raise APIException("You need to specify gender", status_code=400)
        if "dateOfBirth" not in body:
            raise APIException("You need to specify your date of birth", status_code=400)
        if "countryOfBirth" not in body:
            raise APIException("You need to specify your country of birth or N/A", status_code=400)
        if "citizenship" not in body:
            raise APIException("You need to specify your citizenship or N/A", status_code=400)
        if "US_Address" not in body:
            raise APIException("You need to specify your address", status_code=400)
        if "city" not in body:
            raise APIException("You need to specify the city", status_code=400)
        if "state" not in body:
            raise APIException("You need to specify state", status_code=400)
        if "zip" not in body:
            raise APIException("You need to specify zip code", status_code=400)
        if "mobile" not in body:
            raise APIException("You need to specify your phone number or N/A", status_code=400)

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

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if "email" not in body:
            raise APIException("You need to specify the email", status_code=400)
        if "lastname" not in body:
            raise APIException("You need to specify Last Name", status_code=400)
        if "firstname" not in body:
            raise APIException("You need to specify the First Name", status_code=400)
        if "middlename" not in body:
            raise APIException("You need to specify the Middle Name or N/A", status_code=400)
        if "sex" not in body:
            raise APIException("You need to specify sex", status_code=400)
        if "dateOfBirth" not in body:
            raise APIException("You need to specify your date of birth", status_code=400)
        if "countryOfBirth" not in body:
            raise APIException("You need to specify your country of birth or N/A", status_code=400)
        if "citizenship" not in body:
            raise APIException("You need to specify your citizenship or N/A", status_code=400)
        if "US_Address" not in body:
            raise APIException("You need to specify your address", status_code=400)
        if "city" not in body:
            raise APIException("You need to specify the city", status_code=400)
        if "state" not in body:
            raise APIException("You need to specify state", status_code=400)
        if "zip" not in body:
            raise APIException("You need to specify zip code", status_code=400)
        if "mobile" not in body:
            raise APIException("You need to specify your phone number or N/A", status_code=400)


        spouse1 = Spouse(email=body["email"], lastname=body["lastname"], firstname=body["firstname"], middlename=body["middlename"], sex=body["sex"], dateOfBirth=body["dateOfBirth"], countryOfBirth=body["countryOfBirth"], citizenship=body["citizenship"], US_Address=body["US_Address"], city=body["city"], state=body["state"], zip=body["zip"], mobile=body["mobile"])
        db.session.add(spouse1)
        db.session.commit()
        return "ok", 200

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
    if "email" in body:
        spouse1.email = body["email"]
    if "lastname" not in body:
        raise APIException("You need to specify Last Name", status_code=400)
    if "firstname" not in body:
        raise APIException("You need to specify the First Name", status_code=400)
    if "middlename" not in body:
        raise APIException("You need to specify the Middle Name or N/A", status_code=400)
    if "sex" not in body:
        raise APIException("You need to specify sex", status_code=400)
    if "dateOfBirth" not in body:
        raise APIException("You need to specify your date of birth", status_code=400)
    if "countryOfBirth" not in body:
        raise APIException("You need to specify your country of birth or N/A", status_code=400)
    if "citizenship" not in body:
        raise APIException("You need to specify your citizenship or N/A", status_code=400)
    if "US_Address" not in body:
        raise APIException("You need to specify your address", status_code=400)
    if "city" not in body:
        raise APIException("You need to specify the city", status_code=400)
    if "state" not in body:
        raise APIException("You need to specify state", status_code=400)
    if "zip" not in body:
        raise APIException("You need to specify zip code", status_code=400)
    if "mobile" not in body:
        raise APIException("You need to specify your phone number or N/A", status_code=400)

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

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if "application_name" not in body:
            raise APIException("You need to specify the application", status_code=400)

        apps1 = Application(application_name=body['application_name'])
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