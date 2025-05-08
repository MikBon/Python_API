from flask.views import MethodView
from flask_smorest import Blueprint
from flask import request
from passlib.hash import pbkdf2_sha256
from models.user import UserModel
from db import db
from flask_jwt_extended import create_access_token

blp = Blueprint("Users", "users", description="User operations")

@blp.route("/register")
class UserRegister(MethodView):
    def post(self):
        data = request.get_json()
        if UserModel.query.filter_by(username=data["username"]).first():
            return {"message": "User already exists."}, 409

        user = UserModel(
            username=data["username"],
            password=pbkdf2_sha256.hash(data["password"])
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "User created."}, 201

@blp.route("/login")
class UserLogin(MethodView):
    def post(self):
        data = request.get_json()
        user = UserModel.query.filter_by(username=data["username"]).first()

        if user and pbkdf2_sha256.verify(data["password"], user.password):
            access_token = create_access_token(identity=str(user.id))
            return {"access_token": access_token}, 200

        return {"message": "Invalid credentials."}, 401
