from project.extensions import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    cafes = db.relationship("Cafe", backref="users")
    comments = db.relationship("Comment", backref="users")

    def __repr__(self) -> str:
        return f"<User {self.name}>"

