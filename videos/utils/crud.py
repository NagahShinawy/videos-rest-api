"""
created by Nagaj at 15/06/2021
"""

from extensions import db


class AddUpdateDeleteMixin:
    """
    generic for handling crud operation
    """

    def add(self):
        """
        create new obj and save it to db
        :return:
        """
        db.session.add(self)  # pylint: disable=E1101
        db.session.commit()  # pylint: disable=E1101

    def update(self):  # pylint: disable=R0201
        """
        apply updates on an obj
        :return:
        """
        db.session.commit()  # pylint: disable=E1101

    def delete(self):
        """
        delete an obj and commit
        :return:
        """
        db.session.delete(self)  # pylint: disable=E1101
        db.session.commit()  # pylint: disable=E1101
