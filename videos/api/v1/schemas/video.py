"""
created by Nagaj at 15/06/2021
"""

from flask_restful import reqparse, fields

video_post_args = reqparse.RequestParser()
video_post_args.add_argument(
    "name", type=str, help="Name of the video is required", required=True
)

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer,
}