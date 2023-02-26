from flask import Blueprint

from project.extensions import db
from project.models.comment import Comment


comment = Blueprint("comment", __name__)


@comment.route('/comment', methods=["GET", "POST"])
def all_comments():
    return "hello from comment"
