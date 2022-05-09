from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Signup(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired])
    password = StringField('password', validators=[DataRequired])
    confirmpsw = StringField('confirm password', validators=[DataRequired])

class login(FlaskForm):
    Email = StringField('email', validators=[DataRequired])
    password = StringField('password', validators=[DataRequired])