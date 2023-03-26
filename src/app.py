"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from ast import dump
from asyncio.log import logger
import json
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import Favorites, People, Planets, db, User
# from models import Person

import logging
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/users', methods=['GET'])
def handle_hello():

    users = User.query.all()
    users = list(map(lambda x: x.serialize(), users))

    response_body = {
        "data": users
    }

    return jsonify(response_body), 200


@app.route('/user/<id>', methods=['GET'])
def getUser(id):

    user = User.query.get(id)
    if user is None:
        return "Not found"

    user = user.serialize()

    response_body = {
        "data": user
    }

    return jsonify(response_body), 200


@app.route('/favorites', methods=['GET'])
def favoritesAll():

    favorites = Favorites.query.all()
    if favorites is None:
        return "Not found"

    favorites = list(map(lambda x: x.serialize(), favorites))

    response_body = {
        "msg": favorites
    }

    return jsonify(response_body), 200


@app.route('/favorite/<uid>', methods=['GET'])
def getFavorite(uid):

    favorites = Favorites.query.filter_by(uid=uid)

    if favorites is None:
        return "Not found"
    favorites = list(map(lambda x: x.serialize(), favorites))

    response_body = {
        "data": favorites
    }

    return jsonify(response_body), 200


@app.route('/favorite', methods=['POST'])
def saveFavorite():

    data = request.json

    favorite = Favorites(type=data['type'], entityId=int(
        data['entityId']), uid=int(data['uid']))
    db.session.add(favorite)
    db.session.commit()

    response_body = {
        "data": "saved"
    }

    return jsonify(response_body), 200


@app.route('/favorite/<id>', methods=['DELETE'])
def deleteFavorite(id):

    favorite = Favorites.query.get(id)
    db.session.delete(favorite)
    db.session.commit()

    response_body = {
        "data": "deleted"
    }

    return jsonify(response_body), 200

    # --------------------- PEOPLE -----------------


@app.route('/people', methods=['GET'])
def peopleAll():

    people = People.query.all()
    if people is None:
        return "Not found"

    people = list(map(lambda x: x.serialize(), people))

    response_body = {
        "data": people
    }

    return jsonify(response_body), 200


@app.route('/people/<id>', methods=['GET'])
def getPeople(id):

    people = People.query.get(id)

    if people is None:
        return "Not found"
    people = people.serialize()

    response_body = {
        "data": people
    }

    return jsonify(response_body), 200


@app.route('/people', methods=['POST'])
def savePeople():

    data = request.json

    people = People(height=data['height'], name=data['name'],
                    mass=data['mass'], skin_color=data['skin_color'])
    db.session.add(people)
    db.session.commit()

    response_body = {
        "data": "saved"
    }

    return jsonify(response_body), 200


@app.route('/people/<id>', methods=['DELETE'])
def deletePeople(id):

    people = People.query.get(id)
    db.session.delete(people)
    db.session.commit()

    response_body = {
        "data": "deleted"
    }

    return jsonify(response_body), 200

# --------------------- PLANETS -----------------


@app.route('/planets', methods=['GET'])
def planetsAll():

    planets = Planets.query.all()
    if planets is None:
        return "Not found"

    planets = list(map(lambda x: x.serialize(), planets))

    response_body = {
        "data": planets
    }

    return jsonify(response_body), 200


@app.route('/planets/<id>', methods=['GET'])
def getPlanets(id):

    planets = Planets.query.get(id)

    if planets is None:
        return "Not found"
    planets = planets.serialize()

    response_body = {
        "data": planets
    }

    return jsonify(response_body), 200


@app.route('/planets', methods=['POST'])
def savePlanets():

    data = request.json

    planets = Planets(name=data['name'], diameter=data['diameter'],
                      rotation_period=data['rotation_period'], orbital_period=data['orbital_period'],
                      gravity=data['gravity'], gender=data['gender'])
    db.session.add(planets)
    db.session.commit()

    response_body = {
        "data": "saved"
    }

    return jsonify(response_body), 200


@app.route('/planets/<id>', methods=['DELETE'])
def deletePlanets(id):

    planets = Planets.query.get(id)
    db.session.delete(planets)
    db.session.commit()

    response_body = {
        "data": "deleted"
    }

    return jsonify(response_body), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
