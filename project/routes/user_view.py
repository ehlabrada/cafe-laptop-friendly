from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from project.extensions import db
from project.extensions import login_manager
from project.forms import RegisterForm, LoginForm
from project.models.user import User

user = Blueprint("user", __name__, template_folder='../templates/user')


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == int(user_id))).scalar()


@user.route("/all-user", methods=["POST", "GET"])
def get_all_users():
    return "All user"


@user.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()

    if current_user.is_authenticated:
        return redirect(url_for('cafe.home'))

    if request.method == "POST":
        username = register_form.username.data

        user = db.session.execute(db.select(User).where(User.username == username))

        if register_form.validate_on_submit():
            new_user = User(
                name=register_form.name.data,
                username=register_form.username.data,
                password=generate_password_hash(register_form.password.data),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("cafe.home"))
    return render_template("register.html", form=register_form)


@user.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for("cafe.home"))

    if request.method == "POST":
        username = login_form.username.data
        password = login_form.password.data

        if login_form.validate_on_submit():
            user = db.session.execute(db.select(User).where(User.username == username)).scalar()
            print("USER", user)
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("cafe.home"))
            else:
                flash("Sorry, incorrect credentials.")
                return redirect(url_for("user.login"))
    return render_template("login.html", form=login_form)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('cafe.home'))
