from wtforms import Form, BooleanField, BooleanField, StringField, PasswordField, TextField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class RegistrationForm(Form):
    username     = TextField('Username', validators=[DataRequired()])
    email        = TextField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[DataRequired()])

def validate_user(self, username):
	temp_user = User.query.filter_by(username=username.data).first()
	if user is not None:
		raise ValidationError('Username already in use! Please try a different username')

def validate_email(self, email):
	temp_user = User.query.filter_by(email=email.data).first()
	if user is not None:
		raise ValidationError('E-mail already in use! Please try a different e-mail')