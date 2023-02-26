from project.extensions import db


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # Relation with cafe
    cafe_id = db.Column(db.Integer, db.ForeignKey("cafes.id"))
    # cafe = db.relationship("Cafe", backref="comments_cafes", lazy=True)

    # Relation with users
    creator_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # comment_creator = db.relationship('User', backref="comments_list", lazy=True)

    def __repr__(self) -> str:
        return f"<Comment {self.title}>"

