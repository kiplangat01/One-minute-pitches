from wsgiref.validate import validator
from click import confirm
from flask_wtf import FlaskForm
from flask import Flask, render_template
from app import app
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired


# creating user account
class Signup(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired])
    password = StringField('password', validators=[DataRequired])
    confirmpsw = StringField('confirm', validators=[DataRequired])
    submit = SubmitField('Submit')


# user login
class login(FlaskForm):
    Email = StringField('email', validators=[DataRequired])
    password = StringField('password', validators=[DataRequired])


