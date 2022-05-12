from flask import render_template,redirect,url_for,request
from . import main
from .forms import *
from flask_login import login_required,current_user
from .. import db
from ..email import mail_message
from ..models import Pitch,User



@main.route('/')
def index():
    return render_template('index.html')


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Signup_form()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        # mail_message("Welcome to Impressions","email/welcome",user.email,user=user)x
        return redirect(url_for('main.login'))
    return render_template('signup.html', form = form )



@main.route('/login', methods=['GET', 'POST'])
def login():
    login = login_form()
    if request.method == 'POST':
       email = request.form['Email']
       password = request.form['password']
       user = User(email=email, password=password)
    #    mail_message("Welcome to Impressions","email/welcome",user.email,user=user)
       return redirect(url_for('main.pitches'))
    return render_template('login.html', login = login, )



@main.route('/new_pitch',methods=['GET', 'POST'])
@login_required
def new_pitch():
    form =  PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        user_id = current_user._get_current_object().id
        new_pitch = Pitch(pitch=pitch,title =title ,category=category, user_id=user_id)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('pitch.html', form=form)


@main.route('/pitches')
@login_required
def pitches():
    pitches = Pitch.query.all()
    health = Pitch.query.filter_by(category='health').all()
    comedy = Pitch.query.filter_by(category='comedy').all()
    business = Pitch.query.filter_by(category='business').all()
    user = current_user
    return render_template('pitch_display.html', pitches=pitches,  user=user,health=health,comedy=comedy,business=business,)
