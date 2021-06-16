"""
created by Nagaj at 15/06/2021
"""
from flask import Blueprint
from flask_restful import Api  # pylint: disable=E0401

from videos.api.v1.resources.video import VideoListResource, VideoResource
from videos.api.v1.resources.user import UserListResource, UserResource

blueprint = Blueprint("videos", __name__, url_prefix="/api/v1")  # localhost/api/v1/
api = Api(blueprint)

api.add_resource(VideoListResource, "/videos")
api.add_resource(VideoResource, "/videos/<int:id_>")


api.add_resource(UserListResource, "/users/")
api.add_resource(UserResource, "/user/<int:id_>/")
