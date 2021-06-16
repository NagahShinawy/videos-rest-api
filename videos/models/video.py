"""
created by Nagaj at 15/06/2021
"""
from sqlalchemy.sql import func
from extensions import db
from videos.utils.crud import AddUpdateDeleteMixin


class VideoModel(db.Model, AddUpdateDeleteMixin):
    """
    model for video
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False, default=0)
    likes = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, server_default=func.now())

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"
