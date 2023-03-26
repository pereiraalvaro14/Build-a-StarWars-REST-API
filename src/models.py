from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(), unique=False, nullable=True)
    entityId = db.Column(db.Integer(), unique=False, nullable=True)
    uid = db.Column(db.Integer(), unique=False, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "entityId": self.entityId,
            "uid": self.uid
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=False, nullable=False)
    height = db.Column(db.String(), unique=False, nullable=False)
    mass = db.Column(db.String(), unique=False, nullable=False)
    skin_color = db.Column(db.String(), unique=False, nullable=False)
    gender = db.Column(db.PickleType(), unique=False, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.height,
            "gender": self.gender,
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=False, nullable=False)
    diameter = db.Column(db.String(), unique=False, nullable=False)
    rotation_period = db.Column(db.String(), unique=False, nullable=False)
    orbital_period = db.Column(db.String(), unique=False, nullable=False)
    gravity = db.Column(db.PickleType(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            # do not serialize the password, its a security breach
        }
