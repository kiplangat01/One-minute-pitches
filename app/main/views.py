from flask import render_template 
from . import main
from .forms import *
from flask_login import login_required



@main.route('/')
def index():
    return render_template('index.html')


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Signup_form()
    
    return render_template('signup.html', form = form )



@main.route('/login', methods=['GET', 'POST'])
def login():
    login = login_form()
    
    return render_template('login.html', login = login )