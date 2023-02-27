from flask_wtf import FlaskForm
from wtforms.fields import StringField, RadioField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class AddCafeForm(FlaskForm):
    name = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    tables_quantity = IntegerField("Tables", validators=[DataRequired()])
    long_stay = RadioField("Allow Long Stay", validators=[DataRequired()], choices=["Yes", "No"])
    wifi = RadioField("Wifi", validators=[DataRequired()], choices=["Yes", "No"])
    sockets = RadioField("Is there sockets", validators=[DataRequired()], choices=["Yes", "No"])
    quiet = RadioField("Is quiet", validators=[DataRequired()], choices=["Yes", "No"])
    calls = RadioField("Allow calls", validators=[DataRequired()], choices=["Yes", "No"])

    submit = SubmitField("Add cafe")


class RegisterForm(FlaskForm):
    name = StringField("Fullname", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")





























