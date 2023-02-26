from project.extensions import db


class Cafe(db.Model):
    __tablename__ = "cafes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    tables_quantity = db.Column(db.String(100), nullable=False)
    long_stay = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    is_quiet = db.Column(db.Boolean, nullable=False)
    is_allow_calls = db.Column(db.Boolean, nullable=False)





















