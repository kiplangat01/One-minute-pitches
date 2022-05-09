from flask_wtf import FlaskForm

from wtforms import StringField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import DataRequired


# creating user account
class Signup(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirmpsw = PasswordField('confirm', validators=[DataRequired()])
    submit = SubmitField('Submit')


# user login
class login(FlaskForm):
    Email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Submit')

