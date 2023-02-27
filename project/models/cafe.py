from flask_login import UserMixin

from project.extensions import db


class Cafe(db.Model, UserMixin):
    __tablename__ = "cafes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    tables_quantity = db.Column(db.String(100), nullable=False)
    long_stay = db.Column(db.String(3), nullable=False)
    has_wifi = db.Column(db.String(3), nullable=False)
    has_sockets = db.Column(db.String(3), nullable=False)
    is_quiet = db.Column(db.String(3), nullable=False)
    is_allow_calls = db.Column(db.String(3), nullable=False)

    creator_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # cafe_creator = db.relationship("User", backref="cafes_list", lazy=True)

    comments = db.relationship("Comment", backref="cafes", lazy=True)

    def __repr__(self) -> str:
        return f"<Cafe {self.name}>"





















