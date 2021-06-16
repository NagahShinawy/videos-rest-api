"""
created by Nagaj at 15/06/2021
"""

from extensions import db, ma
from videos.models.user import UserModel


class UserSchema(ma.ModelSchema):
    password = ma.String(load_only=True, required=True)

    class Meta:
        model = UserModel
        sqla_session = db.session