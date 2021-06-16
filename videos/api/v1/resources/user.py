"""
created by Nagaj at 15/06/2021
"""
from http import HTTPStatus

from flask import request
from flask_restful import Resource

from extensions import db
from videos.api.v1.schemas.user import UserSchema
from videos.models.user import UserModel


class UserListResource(Resource):
    def get(self):
        schema = UserSchema(many=True)
        qs = UserModel.query.all()
        return {"data": schema.dump(qs).data}, HTTPStatus.OK

    def post(self):
        if not request.is_json:
            return {"msg": "No data"}, HTTPStatus.BAD_REQUEST
        schema = UserSchema()
        user, errors = schema.load(request.get_json())
        if errors:
            return errors, HTTPStatus.UNPROCESSABLE_ENTITY

        qs = UserModel.query.filter(UserModel.name.ilike(request.get_json()["name"]))
        if qs.is_exist():
            return {"msg": "user already exist"}, HTTPStatus.BAD_REQUEST

        user.add()

        return (
            {"msg": "user created", "user": schema.dump(user).data},
            HTTPStatus.CREATED,
        )


class UserResource(Resource):
    """Single object resource
    """

    def get(self, id_):
        """
        get single user by id
        :param id_:
        :return: json user
        """
        schema = UserSchema()
        user = UserModel.query.get_or_404(id_)
        return {"user": schema.dump(user).data}

    def put(self, id_):
        schema = UserSchema(partial=True)
        user = UserModel.query.get_or_404(id_)
        user, errors = schema.load(request.json, instance=user)
        if errors:
            return errors, HTTPStatus.UNPROCESSABLE_ENTITY

        return {"msg": "user updated", "user": schema.dump(user).data}

    def delete(self, id_):
        user = UserModel.query.get_or_404(id_)
        db.session.delete(user)
        db.session.commit()

        return {"msg": "user deleted"}, HTTPStatus.NO_CONTENT
