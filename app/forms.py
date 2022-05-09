from wsgiref.validate import validator
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
    confirmpsw = StringField('confirm password', validators=[DataRequired])
    submit = SubmitField('Submit')


# user login
class login(FlaskForm):
    Email = StringField('email', validators=[DataRequired])
    password = StringField('password', validators=[DataRequired])


@app.route('/form', methods=['GET', 'POST'])
def register():
    name = None
    form = Signup()
    if form.validate_on_submit():
        form.name.data = ''
        
    return render_template('index.html', form=form)
