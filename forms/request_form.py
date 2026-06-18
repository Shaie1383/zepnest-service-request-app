from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms.validators import Optional
from wtforms import DateField, SelectField, StringField, SubmitField, TextAreaField, TimeField
from wtforms.validators import DataRequired, Length


CATEGORY_CHOICES = [
    ("Plumbing", "Plumbing"),
    ("Electrical", "Electrical"),
    ("Cleaning", "Cleaning"),
    ("Painting", "Painting"),
    ("Carpentry", "Carpentry"),
    ("Appliance Repair", "Appliance Repair"),
    ("Other", "Other"),
]

STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("In Progress", "In Progress"),
    ("Completed", "Completed"),
    ("Cancelled", "Cancelled"),
]


class RequestForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[DataRequired(), Length(min=3, max=150)],
    )
    description = TextAreaField(
        "Description",
        validators=[DataRequired(), Length(min=10, max=2000)],
    )
    category = SelectField(
        "Category",
        choices=CATEGORY_CHOICES,
        validators=[DataRequired()],
    )
    address = StringField(
        "Address",
        validators=[DataRequired(), Length(min=10, max=255)],
    )
    preferred_date = DateField(
        "Preferred Service Date",
        format="%Y-%m-%d",
        validators=[DataRequired()],
    )
    preferred_time = TimeField(
        "Preferred Service Time",
        format="%H:%M",
        validators=[DataRequired()],
    )
    status = SelectField(
        "Status",
        choices=STATUS_CHOICES,
        default="Pending",
    )
    image = FileField(
        "Request Image",
        validators=[Optional(), FileAllowed(["jpg", "jpeg", "png"], "Only JPG, JPEG, and PNG images are allowed.")],
    )
    submit = SubmitField("Save Request")
