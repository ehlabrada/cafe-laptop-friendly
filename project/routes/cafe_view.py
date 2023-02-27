from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from project.extensions import db
from project.forms import AddCafeForm
from ..models.cafe import Cafe

cafe = Blueprint('cafe', __name__, template_folder='../templates/cafe')


@cafe.route("/")
def home():
    all_cafes = list(db.session.execute(db.select(Cafe)).scalars())
    print("ALL cafes", all_cafes)
    return render_template("index.html", cafes=all_cafes)


# TODO #2: Add a cafe
@cafe.route('/add-cafe', methods=["GET", "POST"])
@login_required
def add_cafe():
    add_cafe_form = AddCafeForm()
    if request.method == "POST":
        if add_cafe_form.validate_on_submit():
            new_cafe = Cafe(
                name=add_cafe_form.name.data,
                location=add_cafe_form.location.data,
                tables_quantity=add_cafe_form.tables_quantity.data,
                long_stay=add_cafe_form.long_stay.data,
                has_wifi=add_cafe_form.wifi.data,
                has_sockets=add_cafe_form.sockets.data,
                is_quiet=add_cafe_form.quiet.data,
                is_allow_calls=add_cafe_form.calls.data,
                creator_id=1,
            )
            # Add the new cafe to the database
            db.session.add(new_cafe)
            db.session.commit()
            return redirect(url_for("cafe.home"))
    return render_template("create.html", form=add_cafe_form)


@cafe.route("/edit-cafe/<int:id>", methods=["GET", "POST"])
def edit_cafe(id):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == id))
    edit_form = AddCafeForm(
        name=cafe.name,
        location=cafe.location,
        tables_quantity=cafe.tables_quantity,
        long_stay=cafe.long_stay,
        wifi=cafe.wifi,
        sockets=cafe.sockets,
        quiet=cafe.quiet,
        calls=cafe.calls,
    )

    if request.method == "POST":
        if edit_form.validate_on_submit():
            cafe.name = edit_form.name.data
            cafe.location = edit_form.location.data
            cafe.tables_quantity = edit_form.tables_quantity.data
            cafe.long_stay = edit_form.long_stay.data
            cafe.wifi = edit_form.wifi.data
            cafe.sockets = edit_form.sockets.data
            cafe.quiet = edit_form.quiet.data
            cafe.calls = edit_form.calls.data
            db.session.commit()
            return redirect(url_for("cafe.home"))

    return render_template("edit.html", form=edit_form)


@cafe.route("/cafe-detail/<int:id>")
def cafe_detail(id):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
    return render_template("detail.html", cafe=cafe)


@cafe.route("/delete/<int:id>", methods=['GET', 'DELETE'])
@login_required
def delete(id):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == id))
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return redirect(url_for("cafe.home"))
