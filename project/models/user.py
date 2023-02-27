from flask_login import UserMixin

from project.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    cafes = db.relationship("Cafe", backref="user")
    comments = db.relationship("Comment", backref="user")

    def __repr__(self) -> str:
        return f"<User {self.name}>"

