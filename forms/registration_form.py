from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from models.user import User


class RegistrationForm(FlaskForm):
    name = StringField(
        "Full Name",
        validators=[DataRequired(), Length(min=2, max=150)],
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=120)],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8, max=128)],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password", message="Passwords must match.")],
    )
    submit = SubmitField("Create Account")

    def validate_email(self, email):
        existing_user = User.query.filter_by(email=email.data.strip().lower()).first()
        if existing_user:
            raise ValidationError("An account with this email already exists.")
