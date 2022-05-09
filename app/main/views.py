from flask import render_template 
from . import main
from .forms import Signup, login



@main.route('/')
def home():
    return render_template('index.html')


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Signup()
    
    return render_template('signup.html', form = form )



@main.route('/login', methods=['GET', 'POST'])
def signin():
    login_form = login()
    
    return render_template('login.html', login_form = login_form )