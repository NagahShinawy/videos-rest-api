"""
created by Nagaj at 15/06/2021
"""
from extensions import db
from videos.utils.crud import AddUpdateDelete


class VideoModel(db.Model, AddUpdateDelete):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False, default=0)
    likes = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "likes": self.likes,
            "views": self.views,
        }
