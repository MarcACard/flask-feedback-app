from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length, Email


class RegistrationForm(FlaskForm):
    """New User Registration Form"""

    first_name = StringField("First Name", [InputRequired(), Length(max=30)])
    last_name = StringField("Last Name", [InputRequired(), Length(max=30)])
    email = StringField("Email", [InputRequired(), Email(), Length(max=50)])
    username = StringField("Username", [InputRequired(), Length(max=30)])
    password = PasswordField("Password", [InputRequired(), Length(max=30)])


class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField("Username", [InputRequired(), Length(max=30)])
    password = PasswordField("Password", [InputRequired(), Length(max=30)])


class FeedbackForm(FlaskForm):
    """Feedback Form"""

    title = StringField("Title", [InputRequired(), Length(max=100)])
    content = TextAreaField("Feedback", [InputRequired()])
