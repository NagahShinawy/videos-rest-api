"""
created by Nagaj at 15/06/2021
"""
from http import HTTPStatus

from flask_restful import Resource, marshal_with

from videos.api.v1.schemas.video import resource_fields, video_args
from videos.models.video import VideoModel


class VideoResource(Resource):
    """
    get, path, delete for single video
    """

    @marshal_with(resource_fields)
    def get(self, id_):
        """
        get single video by id
        :param id_:
        :return: single video
        """
        video = VideoModel.query.get_or_404(id_)
        return video, HTTPStatus.OK

    @marshal_with(resource_fields)
    def patch(self, id_):
        """
        update the video name
        :param id_: get video by id
        :return: updated video with new name
        """
        video = VideoModel.query.get_or_404(id_)
        json = video_args.parse_args()
        name = json.get("name")
        if name:
            video.name = name
            video.update()
        return video, HTTPStatus.ACCEPTED

    def delete(self, id_):
        """
        delete a video by id
        :param id_: video id
        :return: nothing after video deleting
        """
        video = VideoModel.query.get_or_404(id_)
        video.delete()
        return "", HTTPStatus.NO_CONTENT


class VideoListResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        """
        list of videos
        :return:
        """
        qs = VideoModel.query.all()
        return qs

    @marshal_with(resource_fields)
    def post(self):
        """
        create new video
        :return: new single video
        """
        json = video_args.parse_args()
        video = VideoModel(**json)
        video.add()
        return video, HTTPStatus.CREATED
