from flask import render_template 
from . import pitch
from app.main.forms import *
from wtforms import Form,  StringField,PasswordField, validators
from werkzeug.security import generate_password_hash

@pitch.route('/')
def home():
    return render_template('index.html')


@app.route('/Signup/', methods=['GET', 'POST'])
def signup():
    form = Signup()
    if Signup.method == 'POST' and form.validate():
        if form(form.username.data) is None:
            print('Invalid username')
        else: 
            if form.validate_on_submit():
                return '<h1> the user name is {}. the password is {}.'.format(form.username.data, form.email.data, form.password.data, form.confirmpsw.data)  
            else: 
                print('fill in the spaces')
    return render_template('login.html', title='Login', form=form )