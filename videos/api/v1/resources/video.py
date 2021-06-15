"""
created by Nagaj at 15/06/2021
"""

from flask_restful import Resource, marshal_with

from videos.api.v1.schemas.video import resource_fields, video_post_args
from videos.models.video import VideoModel


class VideoListResource(Resource):

    @marshal_with(resource_fields)
    def get(self):
        return VideoModel.query.all()

    @marshal_with(resource_fields)
    def post(self):
        json = video_post_args.parse_args()
        video = VideoModel(**json)
        video.add()
        return video.to_json()
