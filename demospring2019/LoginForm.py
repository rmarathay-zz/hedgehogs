from wtforms import Form, BooleanField, BooleanField, StringField, PasswordField, validators, TextField

class RegistrationForm(Form):
    username     = TextField('Username', [validators.Length(min=5, max=20)])
    email        = TextField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.Required()])
    password = PasswordField('New Password', [validators.DataRequired()])