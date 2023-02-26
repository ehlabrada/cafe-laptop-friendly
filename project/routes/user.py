from flask import Blueprint

from project.extensions import db
from project.models.user import User


user = Blueprint("user", __name__)


@user.route("/all-users", methods=["POST", "GET"])
def get_all_users():
    return "All users"


