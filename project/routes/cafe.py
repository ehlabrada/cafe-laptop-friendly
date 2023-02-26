from flask import Blueprint, render_template
from project.extensions import db

from ..models.cafe import Cafe


cafe = Blueprint('cafe', __name__)


@cafe.route("/")
def home():
    all_cafes = list(db.session.execute(db.select(Cafe)).scalars())
    return render_template("index.html", cafes=all_cafes)
