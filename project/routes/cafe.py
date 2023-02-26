from flask import Blueprint, render_template
from project.extensions import db

from ..models.cafe import Cafe


cafe = Blueprint('cafe', __name__, template_folder='../templates/cafe')


@cafe.route("/")
def home():
    all_cafes = db.session.execute(db.select(Cafe)).scalars()
    return render_template("index.html", cafes=all_cafes)
