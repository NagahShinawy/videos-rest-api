"""
created by Nagaj at 15/06/2021
"""
from flask import Blueprint
from flask_restful import Api

from videos.api.v1.resources.video import VideoListResource

blueprint = Blueprint("videos", __name__, url_prefix="/api/v1")  # localhost/api/v1/
api = Api(blueprint)

api.add_resource(VideoListResource, "/videos")
