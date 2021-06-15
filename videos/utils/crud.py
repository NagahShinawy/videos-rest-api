"""
created by Nagaj at 15/06/2021
"""


from extensions import db


class AddUpdateDelete:
    def add(self):
        db.session.add(self)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(self)
        return db.session.commit()