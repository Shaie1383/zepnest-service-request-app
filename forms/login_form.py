from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=120)],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8, max=128)],
    )
    remember = BooleanField("Remember me")
    submit = SubmitField("Log In")
