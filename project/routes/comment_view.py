from flask import Blueprint
from flask_login import login_required, current_user

from project.extensions import db
from project.models.comment import Comment


comment = Blueprint("comment", __name__, template_folder='../templates/comment')


@comment.route('/comment', methods=["GET", "POST"])
@login_required
def all_comments():
    return "hello from comment"
